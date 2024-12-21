import scrapy
from nba_stats_collection.items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    
    #This will overwrite the settings 
    custom_settings = {
        'FEEDS': {
            'books_data.json': {'format': 'json', 'overwrite': True}
        }
    }

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()           
            if 'catalogue/' in relative_url:
                book_url = self.start_urls[0] + relative_url
            else:
                book_url = self.start_urls[0] + f'catalogue/{relative_url}'
                
            yield response.follow(book_url, callback=self.parse_book_page)
            
            next_page = response.css('li.next a ::attr(href)').get()
            if next_page:
                if 'catalogue/' in next_page:
                    next_page_url = self.start_urls[0] + next_page
                else:
                    next_page_url = self.start_urls[0] + f'catalogue/{next_page}'

                yield response.follow(next_page_url, callback=self.parse)
    
    def parse_book_page(self, response):
        table_rows = response.css('table tr')
        book_item = BookItem()
        book_item['url'] = response.url
        book_item['title'] = response.css('.product_main h1::text').get()
        book_item['product_type'] = table_rows[1].css('td ::text').get()
        book_item['price_excl_tax'] = table_rows[2].css('td ::text').get()
        book_item['price_incl_tax'] = table_rows[3].css('td ::text').get()
        book_item['tax'] = table_rows[4].css('td ::text').get()
        book_item['num_reviews'] = table_rows[6].css('td ::text').get()
        book_item['stars'] = response.css('p.star-rating').attrib['class']
        book_item['category'] = response.xpath('/html/body/div/div/ul/li[3]/a/text()').get()
        book_item['price'] =  response.css('p.price_color ::text').get()
        yield book_item
        
            
        
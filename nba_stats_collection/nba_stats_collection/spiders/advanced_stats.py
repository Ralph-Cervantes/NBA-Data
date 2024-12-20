import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = [
        'https://quotes.toscrape.com/'  # Example website
    ]

    def parse(self, response):
        # Extract quotes and authors
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").get(),
                'author': quote.css("span small.author::text").get(),
                'tags': quote.css("div.tags a.tag::text").getall(),
            }

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
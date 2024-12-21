import scrapy


class AdvancedStatsSpider(scrapy.Spider):
    name = "advanced_stats"
    allowed_domains = ["www.nba.com"]
    start_urls = ["https://www.nba.com/stats/players/advanced"]

    def parse(self, response):
        pass

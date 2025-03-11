import scrapy
from SP500.items import SP500Item


class SlickchartsSpider(scrapy.Spider):
    name = "slickcharts"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        stock = SP500Item()
        rows = response.xpath("//table[1]/tbody/tr")
        for row in rows:
            stock['number'] = row.xpath("td[1]/text()").get()
            stock['company'] = row.xpath("td[2]/a/text()").get()
            stock['symbol'] = row.xpath("td[3]/a/text()").get()
            stock['ytd_return'] = row.xpath("td[4]/text()").get().replace("\xa0", "").strip()
            yield stock
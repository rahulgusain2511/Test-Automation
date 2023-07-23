import scrapy


class GhostSpiderSpider(scrapy.Spider):
    name = 'ghost_spider'
    allowed_domains = ['toscrape.com']
    # start_urls = ['http://toscrape.com/']

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        e_quote = response.css('.text::text').getall() 
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        yield {'quote': e_quote}

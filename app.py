import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # página de início
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        # quais dados coletar em uma página
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        # qual a próxima página a ir
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
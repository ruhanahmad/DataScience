import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from article_crawler.items import Article
class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Kevin_Bacon']
    
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]
    def parse_info(self, response):
        article = Article()
        
        article['title']: response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        article['url']: response.url
        article['last_edited']: response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
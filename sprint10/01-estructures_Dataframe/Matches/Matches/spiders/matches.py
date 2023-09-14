import scrapy

from Matches.items import MatchesItem
class MatchesSpider(scrapy.Spider):
    name = 'matches'
    #allowed_domains = ['en.wikipedia.org']
    allowed_domains = ['en.wikipedia.org/wiki/2023_FIFA_Women%27s_World_Cup']
    start_urls = ['https://en.wikipedia.org/wiki/2023_FIFA_Women%27s_World_Cup']

    def parse(self, response):
        rows_home = response.xpath('//th[@class="fhome"]')
        rows_away = response.xpath('//th[@class="faway"]')
        rows_score = response.xpath('//th[@class="fscore"]')
        for row_home, row_away, row_score in zip(rows_home,rows_away,rows_score):
            #countries = row.xpath('./span/a//text()').extract()
            item = MatchesItem()
            item['home']= row_home.xpath('./span/a//text()').extract()                        
            item['away']= row_away.xpath('./span/a//text()').extract()
            item['score']= row_score.xpath('./a//text()').extract()
            #yield{
            #    'countries':countries
            #}
            yield item     
          
        pass

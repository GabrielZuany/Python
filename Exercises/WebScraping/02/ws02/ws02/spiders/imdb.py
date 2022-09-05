import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for movies in response.css('.titleColumn '):
            yield{#Gen a dict. Like return.
                'title': movies.css('.titleColumn a::text').get(),#var = response of css class 'titleColumn a' ('::text', means you want only the text). getall()elements found.
                'year': movies.css('.secondaryInfo::text').get(),
                'strong': response.css('strong::text').get()
            }
        pass

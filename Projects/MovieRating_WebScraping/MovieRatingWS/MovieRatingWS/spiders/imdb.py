import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm']

    def parse(self, response):
        
        # Get all movies.
        for mv in response.css('tr'):
            
            # Avoid empty data write.
            if mv.css('.titleColumn a::text').get() != None:
                title = mv.css('.titleColumn a::text').get()
                weekend = mv.css('.ratingColumn::text').get()
                gross = mv.css('.secondaryInfo::text').get()
                weeks = mv.css('.weeksColumn::text').get()
                
                
                # Build a dictionary with the collect data.
                yield{
                    'title': title.strip(),
                    'weekend': weekend.strip(), 
                    'gross': gross.strip(),
                    'weeks': weeks.strip()
                }
                
        pass

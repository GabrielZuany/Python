import scrapy
import datetime

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['br.investing.com']
    start_urls = ['https://br.investing.com/currencies/usd-brl']

    def parse(self, response):
        date = datetime.datetime.now()
        buy = response.css('.trading-hours_value__2MrOn span:nth-child(1)::text').get() 
        sell = response.css('.px-1+ span::text').get()
        buyXsell = buy + '/' + sell
        yield{
            'Last Update': date
        }
        yield{
            'CurrentValue US/BRL': response.css('.font-bold .text-2xl::text').get()
        }
        yield{
            'PreviousValue US/BRL': response.css('.trading-hours_trading-hours-item__BSxaF:nth-child(1) .trading-hours_value__2MrOn::text').get()
        }
        yield{
            'Daily Variation US/BRL': response.css('.trading-hours_trading-hours-item__BSxaF~ .trading-hours_trading-hours-item__BSxaF+ .trading-hours_trading-hours-item__BSxaF .trading-hours_value__2MrOn::text').get()
        }
        yield{
            'Buy x Sell US/BRL': buyXsell
        }
        
        pass

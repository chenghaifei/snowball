import scrapy
import json5


class XqbotSpider(scrapy.Spider):
    name = 'dmtex'
    allowed_domains = ['www.xueqiu.com']
    start_urls = ['https://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=ZH2126346',
        'https://xueqiu.com/P/ZH2126346',
                
    ]

    def parse(self, response):
        # pass
        #print(response.text)
        #page = response.url.split("/")[-1]
       # filename = f'xueqiu{page}.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #    # f.write(response.text)
       # self.log(f'Saved file {filename}')
        html = response.text
        print(html)


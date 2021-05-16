import scrapy
import json5
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response


class XqbotSpider(scrapy.Spider):
    name = 'ttgain'
    allowed_domains = ['www.xueqiu.com']
    start_urls = ['https://xueqiu.com/P/ZH2126346',
    ]

    def parse(self, response):
        headers = {'Referer': 'https://xueqiu.com/P/ZH2126346',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                   'Accept': '*/*',
                   'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                   'Accept-Encoding': 'gzip, deflate, br',
                   #'Content-Type': 'application/json; charset=utf-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   #'Content-Length': 246,
                   'Connection': 'keep-alive',
                   'Host': 'xueqiu.com',
                   'Pragma': 'no-cache'
                   }
        #params = {"filters": []}
        req = scrapy.Request(
            url = 'https://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=ZH2126346',
            #url = '/cubes/nav_daily/all.json?cube_symbol=ZH2126346',
            method = 'GET',
            headers = headers,
            callback = self.parse_ajax
        )
        print(' test again to see  /////////////////////////////// happens')
        print(req)

    def parse_ajax(self, response):
        # yield {'data': response.text}
        inspect_response(response, self)
        self.logger.info("Visited %s", response.url)
        print('this is a ***********************************  !!!')
        #print(response.text)
        #open_in_browser(response)

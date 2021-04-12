import scrapy
import json5


class XqbotSpider(scrapy.Spider):
    name = 'xqbot'
    allowed_domains = ['www.xueqiu.com']
    start_urls = ['https://xueqiu.com/P/ZH2126346',
                'https://xueqiu.com/P/ZH2268976',
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
        pos_start = html.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
        pos_end = html.find('SNB.cubePieData')
        data = html[pos_start:pos_end]
        #print(data)
        data = data.rstrip() # get rid of ending space
        data = data[:-1] # get rid of the last ";"

        dic = json5.loads(data)
        #print('********************')
        #name = dic['name']
        #print(name.encode('utf-8'))
        #print(dic['name'].encode('utf-8'))
        #print('********************')
        scraped_data = {
            'name' : dic['name'],
            'symbol' : dic['symbol'],
            'daily_gain' : dic['daily_gain'],
            'monthly_gain' : dic['monthly_gain'],
            'total_gain' : dic['total_gain'],
            'net_value' : dic['net_value'],
            'rank_percent' : dic['rank_percent'],
            'annualized_gain_rate' : dic['annualized_gain_rate'],
            'bb_rate' : dic['bb_rate'],
        }
        #print(scraped_data)
        yield scraped_data

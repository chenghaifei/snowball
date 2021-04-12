import scrapy
import json5


class XqbotSpider(scrapy.Spider):
    name = 'xqbot'
    allowed_domains = ['www.xueqiu.com']
    start_urls = ['https://xueqiu.com/P/ZH2126346']

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
        data = data.rstrip() # get rid of ending space
        data = data[:-1] # get rid of the last ";"
        dic = json5.loads(data)
        scraped_data = {
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

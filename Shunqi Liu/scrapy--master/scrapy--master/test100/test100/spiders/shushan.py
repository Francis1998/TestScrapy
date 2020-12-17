# encoding=utf-8
__author__ = 'Shunqi Liu'

from scrapy import Request
from scrapy.spiders import Spider
from test100.items import ShushanItem

class ShushanSpider(Spider):
    name = "shushan" #爬虫命名
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    } #代理设置
    def start_requests(self):
        url = 'https://github.com/trending/python?since=monthly&spoken_language_code=en'#访问的初始地址
        cookies = {
            'key': 'value',
            'key': 'value',
            'key': 'value'
        }#可加rookies，但数据量太小，故只用了headers
        yield Request(url, headers=self.headers)
    def parse(self, response):
        item = ShushanItem() #参考Item.py里面的设置，根据爬取的内容项取的名字
        row_all = response.xpath('//div[@class="Box"]/div[2]/article[@class="Box-row"]')[0:10]#获取的是所有item的上层元素位置
        for row in row_all:#定义单个行或块
            item['project_name'] = row.xpath(
                './/h1/a/@href').extract()[0].strip()#获取project_name项的元素位置，并用extract()[0]提取值
            item['num_star'] = row.xpath(
                './/div[2]/a[1]/text()[2]').extract()[0].strip()#获取num_star项的元素位置，并用extract()[0]提取值
            item['num_fork'] = row.xpath(
                './/div[2]/a[2]/text()[2]').extract()[0].strip()# 获取num_fork项的元素位置，并用extract()[0]提取值
            item['main_contributor'] = row.xpath(
                './/div[2]/span[2]/a/@href').extract()[0:5]  # 获取main_contributor项的元素位置，并用extract()[0]提取值
            yield item
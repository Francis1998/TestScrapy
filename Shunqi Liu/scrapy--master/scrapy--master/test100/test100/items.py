# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShushanItem(scrapy.Item):
    # 项目名称
    project_name = scrapy.Field()
    #星数量
    num_star = scrapy.Field()
    #fork数量
    num_fork = scrapy.Field()
    #主要贡献者名称
    main_contributor = scrapy.Field()






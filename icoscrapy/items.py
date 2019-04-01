# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name= scrapy.Field()
    info_href= scrapy.Field()
    rate= scrapy.Field()
    other = scrapy.Field()
    start= scrapy.Field()
    end= scrapy.Field()
    countries= scrapy.Field()
    restrictions_KYC= scrapy.Field()
    whitelist= scrapy.Field()
    page= scrapy.Field()
    subN=scrapy.Field()
    pass

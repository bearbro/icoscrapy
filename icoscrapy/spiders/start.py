#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline

# scrapy crawl itcast （itcast为爬虫名）
cmdline.execute("scrapy crawl listSpider -a beginpage=16 -a endpage=20".split())
#线程数可以在setting.py中设置CONCURRENT_REQUESTS = 1
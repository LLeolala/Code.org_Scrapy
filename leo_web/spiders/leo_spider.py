# leo_spider.py

import scrapy
import json
from selenium import webdriver
class LeoSpider(scrapy.Spider):
    name = 'leo_spider'
    
    def start_requests(self):
        # 读取保存的输入数据
        with open(data['name'], 'r') as f:
            data = json.load(f)
        
        keyword = data['name']
        pages = data['bir']
        
        # 根据输入生成URL (这里用一个示例URL，你需要根据实际情况修改)
        base_url = f"https://code.org/home"
        for i in range(1, pages + 1):
            yield scrapy.Request(url=base_url + str(i), callback=self.parse)

    def parse(self, response):
        # 这里实现你的解析逻辑
        # 例如：
        for item in response.css('div.search-result'):
            yield {
                'title': item.css('h2::text').get(),
                'url': item.css('a::attr(href)').get(),
                'description': item.css('p::text').get()
            }
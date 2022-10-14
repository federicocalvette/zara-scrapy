import scrapy
from zara.items import ZaraItem
from zara.spiders import find_start_urls
import random

class ZaraSpider(scrapy.Spider):
    name = 'zara'
    allowed_domains = ['zara.com']
    start_urls = find_start_urls.get_start_urls()

    lines = open(f'./zara/user_agent_fake.txt').read().splitlines()
    user_agent = random.choice(lines)


    def parse(self, response):
        producto = ZaraItem()
        
        # Extraemos el nombre del producto, la descripcion y su precio
        producto['nombre'] = response.xpath('//h1/text()').extract_first()
        producto['precio'] = response.xpath('//span[@class="money-amount__main"]/text()').extract_first()
        producto['descripcion'] = response.xpath('//div[@class="expandable-text__inner-content"]/p/text()').extract_first()
        
        yield producto
 
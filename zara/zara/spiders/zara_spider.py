import scrapy
from zara.items import ZaraItem

class ZaraSpider(scrapy.Spider):
    name = 'zara'
    allowed_domains = ['zara.com']
    start_urls = [
        'https://www.zara.com/uy/es/camisa-estampado-palmeras-p06085330.html?v1=184203425&v2=2135647',
        'https://www.zara.com/uy/es/camisa-lino---algodon-p01063410.html?v1=177591967&v2=2135647',
        'https://www.zara.com/uy/es/camisa-active-p05445306.html?v1=202796893&v2=2135647',
        'https://www.zara.com/uy/es/camisa-estructura-easy-care-p07545401.html?v1=216142848&v2=2135647'
    ]

    def parse(self, response):
        producto = ZaraItem()
        
        # Extraemos el nombre del producto, la descripcion y su precio
        producto['nombre'] = response.xpath('//h1/text()').extract_first()
        producto['precio'] = response.xpath('//span[@class="money-amount__main"]/text()').extract_first()
        producto['descripcion'] = response.xpath('//div[@class="expandable-text__inner-content"]/p/text()').extract_first()
        
        yield producto
    

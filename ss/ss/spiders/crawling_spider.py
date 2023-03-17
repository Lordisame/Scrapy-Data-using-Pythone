import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import Apartment
import json
import scrapy
from scrapy import Selector



class CrawlingSpider(CrawlSpider) :


    
    name ="mycrawler"
    allowed_domains = ["avito.ma"]
    start_urls = ["https://www.avito.ma/fr/maroc/appartements?o={}".format(i) for i in range(1, 500)]
    
   
    rules = (
        Rule(LinkExtractor(allow=("appartements/")), callback="parse_item", follow=True),
    )
  
    def get_all_links(self, links):
        return [Selector(text=link.get()) for link in links]

    def parse_item(self, response):

        apartment = Apartment()
        apartment['url'] = response.url
        #apartment['image_urls'] = [] 

        """
        Data is obtained inside <script id="__NEXT_DATA__" type="application/json">
        """

        script = response.xpath('//script[@id="__NEXT_DATA__"]').get()
        if script is not None:
            raw_json = script.removeprefix('<script id="__NEXT_DATA__" type="application/json">').removesuffix('</script>')
            obj = json.loads(raw_json)
            if 'props' in obj:
                if 'pageProps' in obj['props']:
                    if 'initialReduxState' in obj['props']['pageProps']:
                        if 'ad' in obj['props']['pageProps']['initialReduxState']:
                            if 'view' in obj['props']['pageProps']['initialReduxState']['ad']:
                                if 'adInfo' in obj['props']['pageProps']['initialReduxState']['ad']['view']:
                                    item_infos = obj['props']['pageProps']['initialReduxState']['ad']['view']['adInfo']
                                    apartment['name'] = item_infos.get('subject', 'N/A')

                                    item_type = item_infos.get('category', 'N/A')
                                    if item_type != 'N/A':
                                        item_type = item_infos['category'].get('name', 'N/A')
                                    apartment['category'] = item_type

                                    price = item_infos.get('price', 'N/A')
                                    if price != 'N/A':
                                        price = item_infos['price'].get('value', 'N/A')
                                    apartment['price']= price

                                    currency = item_infos['price'].get('currency', 'N/A')
                                    apartment['currency'] = currency

                                    apartment['phone'] = item_infos.get('phone', 'N/A')

                                    seller_name = item_infos.get('seller', 'N/A')
                                    if seller_name != 'N/A':
                                        seller_name = item_infos['seller'].get('name', 'N/A')
                                    apartment['seller_name'] = seller_name
                                    
                                    location = item_infos.get('location', None)
                                    if location is not None:
                                        city = location.get('city', 'N/A')
                                        if city != 'N/A':
                                            city = location['city'].get('name', 'N/A')
                                        apartment['city'] = city

                                        area = location.get('area', 'N/A')
                                        if area != 'N/A':
                                            area = 'N/A' if location['area'] is None else location['area'].get('name', 'N/A')
                                        apartment['area'] = area

                                        #apartment['address'] = location.get('address', 'N/A')
                                    description = item_infos.get('description', 'N/A')
                                    apartment['description'] = description.strip()
                                  #  images = item_infos.get('images', None)
                                  #  for image in images:
                                   #     apartment['image_urls'].append(image['fallbackSrc'])                  
        yield apartment
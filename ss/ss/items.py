# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy import Field
import scrapy


class SsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Apartment(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    url = Field()
    name = Field()
    category = Field()
    price = Field()
    currency = Field()
    phone = Field()
    seller_name = Field()
    city = Field()
    area = Field()
    description = Field()

    #address = Field()
    #image_urls = Field()
    #images = Field()
    
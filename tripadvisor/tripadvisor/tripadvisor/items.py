# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    comment_author = scrapy.Field()
    address_author = scrapy.Field()
    title_comment = scrapy.Field()
    body_comment = scrapy.Field()

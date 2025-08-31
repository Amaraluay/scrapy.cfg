import scrapy

class StepstoneLeadsItem(scrapy.Item):
    keyword = scrapy.Field()
    location = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    jobs = scrapy.Field()
    profile = scrapy.Field()

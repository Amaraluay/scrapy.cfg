import scrapy

class StepstoneSpider(scrapy.Spider):
    name = "stepstone"

    def start_requests(self):
        url = "https://www.stepstone.de/jobs/servicetechniker/in-stuttgart?radius=50"
        yield scrapy.Request(url, meta={"playwright": True}, callback=self.parse)

    async def parse(self, response):
        # deine Logik rein
        self.logger.info("Seite geladen: %s", response.url)

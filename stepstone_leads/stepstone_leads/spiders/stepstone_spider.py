import scrapy
from scrapy_playwright.page import PageMethod
from ..items import StepstoneLeadsItem

class StepstoneSpider(scrapy.Spider):
    name = "stepstone"

    def start_requests(self):
        url = "https://www.stepstone.de/jobs/servicetechniker/in-stuttgart?radius=50"
        yield scrapy.Request(
            url,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_load_state", "domcontentloaded"),
                    PageMethod("click", "#ccmgt_explicit_accept", timeout=3000, strict=False),
                ],
            },
            callback=self.parse,
        )

    async def parse(self, response):
        # Beispiel: Zählt Jobkarten
        cards = response.css("article[data-at='job-item']")
        self.logger.info("Gefundene Jobs: %s", len(cards))

        for card in cards:
            title = card.css("[data-testid='job-item-title'] ::text").get()
            company = card.css("span[data-at='job-item-company-name'] ::text").get()
            if not company:
                continue

            yield StepstoneLeadsItem(
                keyword="servicetechniker",
                location="stuttgart",
                title=(title or "").strip(),
                company=company.strip(),
                jobs=0,
                profile=response.url,
            )

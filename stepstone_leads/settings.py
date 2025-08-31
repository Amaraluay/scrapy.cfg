BOT_NAME = "stepstone_leads"

SPIDER_MODULES = ["stepstone_leads.spiders"]
NEWSPIDER_MODULE = "stepstone_leads.spiders"

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True, "args": ["--no-sandbox"]}

# Output
FEEDS = {"leads.csv": {"format": "csv", "overwrite": True}}

BOT_NAME = "stepstone_leads"

SPIDER_MODULES = ["stepstone_leads.spiders"]
NEWSPIDER_MODULE = "stepstone_leads.spiders"

# Playwright-Integration
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True, "args": ["--no-sandbox"]}

# Performance
CONCURRENT_REQUESTS = 8
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000
DOWNLOAD_TIMEOUT = 45
RETRY_ENABLED = True
RETRY_TIMES = 3
AUTOTHROTTLE_ENABLED = True

# Pipelines (noch leer)
ITEM_PIPELINES = {
   "stepstone_leads.pipelines.StepstoneLeadsPipeline": 300,
}

# Output-Datei (mit Timestamp überschreibbar)
from datetime import datetime
FEEDS = {
    f"leads_{datetime.now():%Y%m%d_%H%M%S}.csv": {"format": "csv", "overwrite": True},
}

# Resume nach Abbruch
JOBDIR = ".jobdir"

# Roms Universe Scrapy Spider

Scrapes the Roms from Roms Universe.

## Running

By default, will scrape every rom for every platform available.

    scrapy crawl romsuniverse

To filter down to specific platforms, use the "platforms" argument
with a comma-separated list of platforms to scrape.

    scrape crawl romsuniverse -a platforms=playstation-2,xbox

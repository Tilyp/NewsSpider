from scrapy import cmdline


cmdline.execute("scrapy crawl SinaSpider --logfile log/Sina.log".split())
# cmdline.execute("scrapy crawl SinaSpider".split())

# cmdline.execute("scrapy crawl SoGouSpider --logfile log/SoGou.log".split())
# cmdline.execute("scrapy crawl SoGouSpider".split())

# cmdline.execute("scrapy crawl SinaMsgSpider".split())

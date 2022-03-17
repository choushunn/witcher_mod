from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'witcher', '-o', 'data.csv', '-s', 'FEED_EXPORT_ENCODING=utf-8'])
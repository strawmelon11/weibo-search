from scrapy import cmdline

# 不用前面的记录爬取
# cmdline.execute('scrapy crawl search'.split())

# 基于之前运行的代码继续爬取
cmdline.execute('scrapy crawl search -s JOBDIR=crawls/search'.split())
from scrapy import cmdline
 
cmdline.execute('scrapy crawl txms'.split())
# cmdline.execute('scrapy crawl txms -o TXmovies.csv'.split())
# cmdline.execute('scrapy crawl txms -o TXmovies.json'.split())
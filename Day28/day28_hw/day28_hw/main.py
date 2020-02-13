import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1581581923.A.CF8.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581581967.A.43C.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1581581968.A.A93.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('crawler_api', start_urls=target_urls, filename='day28.json')
    process.start()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Zach | Last Place Comics | Twitter'
    BASE_URL = 'https://twitter.com/lastplacecomics'
    ENABLE = True
    SCREEN_NAME = 'lastplacecomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

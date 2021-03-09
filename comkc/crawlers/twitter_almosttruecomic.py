# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Almost True Stories | Twitter'
    BASE_URL = 'https://twitter.com/almosttruecomic'
    ENABLE = True
    SCREEN_NAME = 'almosttruecomic'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

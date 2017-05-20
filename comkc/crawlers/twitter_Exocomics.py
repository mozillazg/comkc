# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Li Chen | Twitter'
    BASE_URL = 'https://twitter.com/Exocomics'
    ENABLE = True
    SCREEN_NAME = 'Exocomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

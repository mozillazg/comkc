# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Things in Squares | Twitter'
    BASE_URL = 'https://twitter.com/tiscomics'
    ENABLE = True
    SCREEN_NAME = 'tiscomics'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

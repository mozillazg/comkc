# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Charlie Higson | Twitter'
    BASE_URL = 'https://twitter.com/CPHigson'
    ENABLE = True
    SCREEN_NAME = 'CPHigson'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

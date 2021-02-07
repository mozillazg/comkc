# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'eldercactus | Twitter'
    BASE_URL = 'https://twitter.com/eldercactus'
    ENABLE = True
    SCREEN_NAME = 'eldercactus'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

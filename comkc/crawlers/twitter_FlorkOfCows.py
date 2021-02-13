# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Flork | Twitter'
    BASE_URL = 'https://twitter.com/FlorkOfCows'
    ENABLE = False
    SCREEN_NAME = 'FlorkOfCows'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

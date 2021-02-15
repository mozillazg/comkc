# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'False Knees | Twitter'
    BASE_URL = 'https://twitter.com/FalseKnees'
    ENABLE = True
    SCREEN_NAME = 'FalseKnees'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

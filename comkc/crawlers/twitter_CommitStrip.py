# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'CommitStrip | Twitter'
    BASE_URL = 'https://twitter.com/CommitStrip'
    ENABLE = True
    SCREEN_NAME = 'CommitStrip'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

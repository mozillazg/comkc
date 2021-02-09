# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'cee | Twitter'
    BASE_URL = 'https://twitter.com/relatabledoodle'
    ENABLE = True
    SCREEN_NAME = 'relatabledoodle'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

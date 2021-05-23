# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'The Jenkins | Twitter'
    BASE_URL = 'https://twitter.com/thejenkinscomic'
    ENABLE = True
    SCREEN_NAME = 'thejenkinscomic'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'i love you | Twitter'
    BASE_URL = 'https://twitter.com/WordsText'
    ENABLE = True
    SCREEN_NAME = 'WordsText'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

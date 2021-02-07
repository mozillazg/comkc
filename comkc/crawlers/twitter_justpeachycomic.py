# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Just Peachy Comic | Twitter'
    BASE_URL = 'https://twitter.com/justpeachycomic'
    ENABLE = True
    SCREEN_NAME = 'justpeachycomic'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

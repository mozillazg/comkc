# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'Sven In Frames | Twitter'
    BASE_URL = 'https://twitter.com/SvenInFrames'
    ENABLE = True
    SCREEN_NAME = 'SvenInFrames'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

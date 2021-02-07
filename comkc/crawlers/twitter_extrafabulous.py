# -*- coding: utf-8 -*-
from comkc.crawlers._twitter_crawler import TwitterWorker


class Worker(TwitterWorker):
    SITE = 'zach | Twitter'
    BASE_URL = 'https://twitter.com/extrafabulous'
    ENABLE = True
    SCREEN_NAME = 'extrafabulous'


if __name__ == '__main__':
    from comkc.crawlers._twitter_crawler import main
    main(Worker)

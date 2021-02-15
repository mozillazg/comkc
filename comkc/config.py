# -*- coding: utf-8 -*-
import logging
import os

PG_DSN = os.environ['COMKC_PG_DSN']
DEBUG = (os.getenv('COMKC_DEBUG') == 'true')

STORAGE_API_URL = os.getenv('COMKC_STORAGE_API_URL')
STORAGE_API_TOKEN = os.getenv('COMKC_STORAGE_API_TOKEN')
STORAGE_URL_FORMAT = os.getenv('COMKC_STORAGE_URL_FORMAT')

WORKER_SLEEP = int(os.getenv('COMKC_WORKER_SLEEP', 60 * 60 * 6))
MAX_LIMIT = 20
MAX_OFFSET = 500

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.INFO

format_str = '%(levelname)s %(asctime)s %(module)s %(name)s %(message)s'
logging.basicConfig(level=level, format=format_str)

SENTRY_DSN = os.environ.get('COMKC_SENTRY_DSN')
if SENTRY_DSN:
    from raven.conf import setup_logging
    from raven.handlers.logging import SentryHandler
    handler = SentryHandler(SENTRY_DSN)
    handler.setLevel(logging.ERROR)
    setup_logging(handler)


TWITTER = {
    'consumer_key': os.environ.get('COMKC_TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.environ.get('COMKC_TWITTER_CONSUMER_SECRET'),
    'access_token': os.environ.get('COMKC_TWITTER_ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('COMKC_TWITTER_ACCESS_TOKEN_SECRET'),
}
peony_client = None
if TWITTER['consumer_key']:
    from peony import PeonyClient
    peony_client = PeonyClient(**TWITTER)

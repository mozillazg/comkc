# -*- coding: utf-8 -*-
import logging
import os

PG_DSN = os.environ['COMKC_PG_DSN']
DEBUG = (os.getenv('COMKC_DEBUG') == 'true')

QINIU = {
    'access_key': os.getenv('COMKC_QINIU_ACCESS_KEY'),
    'secret_key': os.getenv('COMKC_QINIU_SECRET_KEY'),
    'bucket_name': os.getenv('COMKC_QINIU_BUCKET_NAME'),
    'url_format': os.getenv('COMKC_QINIU_URL_FORMAT'),
}

WORKER_SLEEP = 60 * 60 * 8
MAX_LIMIT = 20
MAX_OFFSET = 10

if DEBUG:
    level = logging.DEBUG
else:
    level = logging.INFO

SENTRY_DSN = os.environ.get('COMKC_SENTRY_DSN')
if SENTRY_DSN:
    from raven.conf import setup_logging
    from raven.handlers.logging import SentryHandler
    handler = SentryHandler(SENTRY_DSN)
    setup_logging(handler)

format_str = '%(levelname)s %(asctime)s %(module)s %(name)s %(message)s'
logging.basicConfig(level=level, format=format_str)


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

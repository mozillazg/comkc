# -*- coding: utf-8 -*-
import asyncio
import glob
import logging
import os

from comkc.crawlers import crawlers

logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.realpath(__file__))

for path in glob.glob(
    os.path.join(current_dir, 'crawlers') + os.path.sep + '*.py'
):
    if '__init__' in path:
        continue
    module = 'comkc.crawlers.{}'.format(os.path.basename(path).split('.')[0])
    if module.endswith('.archive'):
        continue
    __import__(module)


async def main(loop):
    futures = []
    for name, cls in crawlers.items():
        logger.info('got an crawler: %s from module %s', name, cls.__module__)
        future = asyncio.ensure_future(cls().run())
        futures.append(future)
    await asyncio.wait(futures)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()

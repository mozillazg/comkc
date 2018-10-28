# -*- coding: utf-8
import asyncio
import logging
import io

from aiopg.sa import create_engine
import aiohttp

from comkc import config, models
from comkc.utils import fetch_url

dsn = config.PG_DSN
logger = logging.getLogger(__name__)


async def upload(data, comic):
    async with aiohttp.ClientSession() as session:
        data = {
            'file': io.BytesIO(data),
        }
        headers = {
            'Token': config.STORAGE_API_TOKEN,
        }
        async with session.post(
                config.STORAGE_API_URL,
                data=data, headers=headers) as resp:
            ret = await resp.json()

    return config.STORAGE_URL_FORMAT.format(filename=ret['key'])


async def upload_images():
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            comics = await models.list_comics(
                conn, (models.table_comic.c.cdn == ''),
                limit=1000
            )
            for comic in comics:
                image_url = comic['image']
                try:
                    image_data = await fetch_url(image_url, binary=True)
                    assert image_data
                except Exception as e:
                    logger.exception('download %s failed! \n%s', image_url, e)
                    continue
                try:
                    cdn_url = await upload(image_data, comic)
                except Exception as e:
                    logger.exception('upload %s failed! \n%s', image_url, e)
                    continue

                uuid = str(comic['uuid'])
                await models.update_comics(
                    conn, (models.table_comic.c.uuid == uuid), cdn=cdn_url
                )
                logger.info('download %s then upload to %s success!',
                            image_url, cdn_url)
                await asyncio.sleep(60 * 1)


async def main(loop):
    while True:
        await upload_images()
        await asyncio.sleep(config.WORKER_SLEEP / 3)


if __name__ == '__main__':
    if config.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO
    format_str = '%(levelname)s %(asctime)s %(module)s %(name)s %(message)s'
    logging.basicConfig(level=level, format=format_str)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    except KeyboardInterrupt:
        loop._run_once()
        loop.stop()
    finally:
        loop.close()

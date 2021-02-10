# -*- coding: utf-8
import asyncio
import logging
import io

from aiopg.sa import create_engine
import aiohttp
from PIL import Image

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
                # conn, (models.table_comic.c.site == 'webcomic name'),
                limit=10000
            )
            for comic in comics:
                image = comic['image']
                images = image.split(' ')
                data_list = []

                for image_url in images:
                    if image_url.startswith('http://https://'):
                        image_url = image_url[len('http://'):]
                    if '://' not in image_url:
                        logger.error('find an invalid image(%s) from %r',
                                     image_url, comic)
                        continue
                    try:
                        image_data = await fetch_url(image_url, binary=True)
                        if b'<html' in image_data:
                            image_data = await fetch_url(
                                image_url, binary=True,
                                referer=comic['source'])
                        assert image_data
                        data_list.append(image_data)
                    except Exception as e:
                        logger.exception(
                                'download %s failed! \n%s', image_url, e)
                        continue

                if not data_list:
                    continue
                elif len(data_list) == 1:
                    image_data = data_list[0]
                else:
                    image_data = merge_images(data_list)

                try:
                    cdn_url = await upload(image_data, comic)
                except Exception as e:
                    logger.exception('upload %s failed! (%r) \n%s',
                                     image, comic, e)
                    continue

                uuid = str(comic['uuid'])
                await models.update_comics(
                    conn, (models.table_comic.c.uuid == uuid), cdn=cdn_url
                )
                logger.info('download %s then upload to %s success!',
                            image, cdn_url)
                await asyncio.sleep(60 * 1)


def merge_images(image_list):
    middle_height = 20
    images = [Image.open(io.BytesIO(x)) for x in image_list]
    width = max(x.width for x in images)
    height = sum(x.height for x in images) + (len(images) + 1) * middle_height
    dst = Image.new('RGB', (width, height), 'white')

    h = middle_height
    for im in images:
        dst.paste(im, (0, h))
        h = h + im.height + middle_height - 2

    dst_data = io.BytesIO()
    dst.save(dst_data, format='jpeg')
    return dst_data.getvalue()


def fix_image_url(comic, image_url):
    pass


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

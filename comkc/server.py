# -*- coding: utf-8 -*-
import datetime
import functools
import json
import os
import uuid

from aiohttp import web
from aiopg.sa import create_engine

from comkc import config, models

app = web.Application()
dsn = config.PG_DSN
current_dir = os.path.dirname(os.path.realpath(__file__))


def json_dump_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.ctime()
    if isinstance(obj, uuid.UUID):
        return obj.hex
    raise TypeError(obj)


json_dumps = functools.partial(json.dumps, default=json_dump_default, indent=2)
json_response = functools.partial(web.json_response, dumps=json_dumps)


def validate_uuid(uuid_str):
    try:
        value = uuid.UUID(uuid_str, version=4)
    except ValueError:
        return False
    return value.hex == uuid_str


async def list_comics(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            limit = 10
            offset = 0
            per_page = request.query.get('per_page', '8')
            page = request.query.get('page', '1')
            if per_page.isdigit() and int(per_page) > 0:
                if int(per_page) < config.MAX_LIMIT:
                    limit = int(per_page)
            if page.isdigit() and int(page) > 0:
                if int(page) < config.MAX_OFFSET:
                    offset = (int(page) - 1) * limit
                if offset > 0:
                    offset += 1

            where = [
            ]
            site = request.query.get('site')
            if site:
                where.append(models.table_comic.c.site == site)
            random = request.query.get('random')
            if random:
                order_by = 'random()'
            else:
                order_by = models.table_comic.c.posted_at.desc()
            comics = await models.list_comics(
                conn, *where, limit=limit, offset=offset, order_by=order_by
            )
            return json_response(comics)


async def list_sites(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            titles = await models.list_sites(conn)
            return json_response(titles)


async def get_comic(request):
    async with create_engine(dsn) as engine:
        async with engine.acquire() as conn:
            uuid = request.match_info['uuid']
            if not validate_uuid(uuid):
                return json_response({}, status=404)

            where = (models.table_comic.c.uuid == uuid)
            comic = await models.get_comic(conn, where)
            if comic is not None:
                return json_response(comic)
            else:
                return json_response({}, status=404)

app.router.add_route('GET', '/api/v1/comics/', list_comics)
app.router.add_route('GET', '/api/v1/comics/sites/', list_sites)
app.router.add_route('GET', '/api/v1/comics/{uuid}', get_comic)

if __name__ == '__main__':
    app.router.add_static(
            '/', os.path.join(current_dir, '../new_frontend/build/'),
            show_index=True)
    web.run_app(app, host='0.0.0.0', port=8080)

# -*- coding: utf-8 -*-
import datetime

import sqlalchemy
import sqlalchemy.dialects.postgresql
from sqlalchemy.sql import select
import sqlalchemy.types

metadata = sqlalchemy.MetaData()

table_comic = sqlalchemy.Table(
    'comics', metadata,
    sqlalchemy.Column('uuid', sqlalchemy.dialects.postgresql.UUID,
                      server_default=sqlalchemy.text('gen_random_uuid()')),
    sqlalchemy.Column('site', sqlalchemy.String),
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('source', sqlalchemy.String),
    sqlalchemy.Column('image', sqlalchemy.String),
    sqlalchemy.Column('cdn', sqlalchemy.String, server_default='""'),
    sqlalchemy.Column('posted_at', sqlalchemy.types.TIMESTAMP),
    sqlalchemy.Column('created_at', sqlalchemy.types.TIMESTAMP),
)


async def insert_comic(conn, data: dict):
    sql = table_comic.insert().values(
        created_at=datetime.datetime.now(), **data
    )
    return await conn.execute(sql)


async def get_comic(conn, *where):
    sql = select([table_comic]).where(*where)
    async for row in conn.execute(sql):
        return dict(row)


async def list_comics(conn, *where, limit: int=10, offset: int=0,
                      order_by=None):
    sql = select([table_comic])
    if where:
        sql = sql.where(*where)
    if order_by is None:
        order_by = table_comic.c.posted_at.desc()
    if offset > 0:
        sql = sql.offset(offset)
    sql = sql.order_by(order_by).limit(limit)
    result = []

    async for row in conn.execute(sql):
        result.append(dict(row))
    return result


async def update_comics(conn, *where, **values):
    sql = table_comic.update()
    if where:
        sql = sql.where(*where)
    sql = sql.values(**values)
    return await conn.execute(sql)


def create_db(name_or_uri):
    engine = sqlalchemy.create_engine(name_or_uri)
    metadata.create_all(engine)

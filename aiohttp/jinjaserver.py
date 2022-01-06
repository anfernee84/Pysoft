import logging
from sqlite3.dbapi2 import connect
import jinja2
import aiohttp_jinja2
from aiohttp import web
import asyncio
import aiosqlite



@aiohttp_jinja2.template("view.html")
class HomeHandler(web.View):

    async def get(request):
        try:
            db = await aiosqlite.connect ("collected_data.db")
            db.row_factory = aiosqlite.Row
            cursor = await db.execute("select * from parsedata")
            data = await cursor.fetchall()
            recds = [dict(q) for q in data]
            return {'rows': data}
        except Exception as error:
            print ('Error: ', error.args)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)
    app = web.Application()
    aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader('templates'))
    app.router.add_get('/', HomeHandler, name="view")
    web.run_app(app, host="0.0.0.0")


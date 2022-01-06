import asyncio
from time import time
from timeit import default_timer
from aiohttp import ClientSession
import sqlite3


def fetch_async(urls):
    start_time = default_timer()

    loop = asyncio.get_event_loop() 
    future = asyncio.ensure_future(fetch_all(urls)) 
    loop.run_until_complete(future) 

    tot_elapsed = default_timer() - start_time
    print('Total time taken : ' + str(tot_elapsed) + " seconds")

async def fetch_all(urls):
    tasks = []
    fetch.start_time = dict() 
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task) 
        _ = await asyncio.gather(*tasks) 

async def fetch(url, session):
    # fetch.start_time[url] = default_timer()
    async with session.get(url) as response:
        fetch.start_time[url] = default_timer()
        r = await response.read()
        elapsed = default_timer() - fetch.start_time[url]
        rtime = url  + 'response time = ' + str(elapsed) + " mseconds"
        status = response.status
        ctype = response.headers["Content-type"]
        sdate = response.headers['date']
        wsrv = response.headers['Server']
        scookie = response.headers["Set-Cookie"]
        print (f'{rtime} \nStatus: {status} \nContent-type: {ctype} \nServer date: {sdate} \nWeb server: {wsrv} \nCookie settings: {scookie}' '\n')
        with sqlite3.connect("collected_data.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""insert into parsedata (URL,TimeResponse,SiteResponse,ConType,SrvDate,WebSrv,Csettings) values(?,?,?,?,?,?,?);""",(url,elapsed,status,ctype,sdate,wsrv,scookie))
            connection.commit()

        return r



if __name__ == '__main__':
    with open ("sites.txt", "r") as fh:
        urls = fh.readlines()
    fetch_async(urls)
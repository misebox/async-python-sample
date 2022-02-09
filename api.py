import asyncio
import time

from fastapi import FastAPI
from fastapi import Query


app = FastAPI(title='async-python')


@app.get('/{no}')
async def slow_resource(no: int =0):
    t1 = time.perf_counter()
    await asyncio.sleep(no % 3 + 1)
    t2 = time.perf_counter()
    interval = int((t2 - t1) * 1000) / 1000
    return {"no": no, "interval": interval}


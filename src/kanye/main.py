__version__ = "0.1"

import httpx
import asyncio

client = httpx.AsyncClient(base_url="https://api.kanye.rest")

async def _get_data() -> str:

    res = (await client.get('/text')).content
    return res.decode('utf-8')

async def GetQuote(n:int) -> list[str]:
    awaitables = [_get_data() for i in range(n)]
    return await asyncio.gather(*awaitables)

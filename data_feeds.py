import aiohttp

class DexScreenerAPI:
    async def get_trending(self):
        url = "https://api.dexscreener.com/latest/dex/tokens/trending"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

class CoinGeckoAPI:
    async def get_trending(self):
        url = "https://api.coingecko.com/api/v3/search/trending"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

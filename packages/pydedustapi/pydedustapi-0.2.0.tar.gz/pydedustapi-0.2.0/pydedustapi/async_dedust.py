from requests import get
import aiohttp
import asyncio

class AsyncDedust:
        def __init__(self):
                self.baseUrl = 'https://api.dedust.io'
                self.headers = {"Accept": "application/json"}

        async def get_liquidity_providers_v1(self, address):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.base_url}/v1/pools/{address}/liquidity-providers', headers=self.headers) as response:
                                return await response.json()

        async def get_accounts_assets(self, address):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.base_url}/v2/accounts/{address}/assets', headers=self.headers) as response:
                                return await response.json()

        async def get_accounts_trades(self, address):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.base_url}/v2/accounts/{address}/trades', headers=self.headers) as response:
                                return await response.json()

        async def get_assets(self):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.base_url}/v2/assets', headers=self.headers) as response:
                                return await response.json()

        async def get_assets_symbol(self, symbol):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.base_url}v2/assets/{symbol}', headers=self.headers) as response:
                                return await response.json()
                        
        async def get_gcko_pairs(self):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/gcko/pairs', headers=self.headers) as response:
                                return await response.json()
        
        async def get_gcko_tickers(self):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/gcko/tickers', headers=self.headers) as response:
                                return await response.json()
        
        async def get_gcko_trades(self, ticker_id, type, limit):
                async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/gcko/trades?ticker_id={ticker_id}&type={type}&limit={limit}', headers=self.headers) as response:
                                return await response.json()
        
        async def get_jettons_metadata(self, address):
                async with aiohttp.ClientSession() as session:      
                        async with session.get(f'{self.baseUrl}/v2/jettons/{address}/metadata', headers=self.headers) as response:
                                return await response.json()
        
        async def get_pools(self):
            async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/pools', headers=self.headers) as response:
                                return await response.json()
        
        async def get_pools_metadata(self, address):
            async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/pools/{address}/metadata', headers=self.headers) as response:
                                return await response.json()
        
        async def get_pools_trades(self, address):
            async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/pools/{address}/trades', headers=self.headers) as response:
                                return await response.json()
        
        async def get_prices(self):
            async with aiohttp.ClientSession() as session:
                        async with session.get(f'{self.baseUrl}/v2/prices', headers=self.headers) as response:
                                return await response.json()
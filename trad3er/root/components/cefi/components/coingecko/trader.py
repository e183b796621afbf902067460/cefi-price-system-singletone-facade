import requests
from typing import Optional
import time

from trad3er.interfaces.trader.interface import iTrad3r


class CoinGeckoTrad3r(iTrad3r):
    _endpoint = "https://api.coingecko.com/api/v3/simple/price?ids={first}&vs_currencies={second}"

    _markets: dict = {
        'USDT': 'tether',
        'WETH': 'weth',
        'WBNB': 'wbnb',
        'WBTC': 'wrapped-bitcoin',
        'amWETH': 'aave-polygon-weth',
        'amWBTC': 'aave-polygon-wbtc',
        'gDAI': 'geist-dai',
        'gUSDC': 'geist-usdc',
        'gfUSDT': 'geist-fusdt',
        'GUSD': 'gemini-dollar',
        'TUSD': 'true-usd',
        'FEI': 'fei-usd',
        'USDP': 'paxos-standard',
        'LUSD': 'liquity-usd',
        'MIM': 'magic-internet-money',
        'EPX': 'ellipsis-x',
        'sUSD': 'nusd',
        'UST': 'terrausd-wormhole',
        'AMPL': 'ampleforth',
        'DPI': 'defipulse-index',
        'renFIL': 'renfil',
        'stETH': 'staked-ether',
        'xSUSHI': 'xsushi',
        'WFTM': 'wrapped-fantom',
        'WAVAX': 'wrapped-avax',
        'JOE': 'joe',
        'GEIST': 'geist-finance',
        'WXT': 'wirex'
    }

    @classmethod
    def get_price(cls, first: str, second: str, *args, **kwargs) -> Optional[float]:
        second = 'usd' if second == 'USD' else second
        try:
            first = cls._markets[first]
            r = requests.get(url=cls._endpoint.format(first=first, second=second))
            while r.status_code == 429:
                time.sleep(10)
                r = requests.get(url=cls._endpoint.format(first=first, second=second))
            return r.json()[first][second]
        except KeyError:
            return None

import requests
from typing import Optional
import time

from head.interfaces.trader.interface import ITraderComponent


class CoingeckoTrader(ITraderComponent):
    _endpoint = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"

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
    def getPrice(self, major: str, vs: str, *args, **kwargs) -> Optional[float]:
        vs = 'usd' if vs == 'USD' else vs
        try:
            market = self._markets[major]
            r = requests.get(url=self._endpoint.format(market, vs))
            while r.status_code == 429:
                time.sleep(10)
                r = requests.get(url=self._endpoint.format(market, vs))
            return r.json()[market][vs]
        except KeyError:
            return None

import requests
from typing import Optional

from trad3er.interfaces.trader.interface import iTrad3r


class BinanceTrad3r(iTrad3r):

    _endpoint = "https://api.binance.com/api/v3/ticker/price?symbol="
    _sames: dict = {
        'fUSDT': 'USDT',
        'DAI.e': 'DAI',
        'USDT.e': 'USDT',
        'USDC.e': 'USDC',
        'WETH.e': 'ETH',
        'WBTC.e': 'WBTC',
        'CRV.e': 'CRV',
        'WETH': 'ETH',
        'WBNB': 'BNB',
        'WBTC': 'BTC',
        'WFTM': 'FTM',
        'WMATIC': 'MATIC'
    }

    @classmethod
    def _same(cls, asset: str) -> str:
        return cls._sames[asset] if asset in cls._sames else asset

    @classmethod
    def get_price(cls, first: str, second: str, *args, **kwargs) -> Optional[float]:
        second = 'usdt' if second == 'USD' else second
        first = cls._same(asset=first)
        try:
            return float(requests.get(url=cls._endpoint + first.upper() + second.upper()).json()['price'])
        except KeyError:
            return None

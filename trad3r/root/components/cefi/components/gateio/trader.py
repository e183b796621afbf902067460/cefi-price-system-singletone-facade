import requests
from typing import Optional

from trad3r.interfaces.trader.interface import iTrad3r


class GateIOTrad3r(iTrad3r):

    _endpoint = "https://api.gateio.ws/api/v4/spot/tickers?currency_pair={first}_{second}"
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
            return float(requests.get(url=cls._endpoint.format(first=first.upper(), second=second.upper())).json()[0]['last'])
        except KeyError:
            return None

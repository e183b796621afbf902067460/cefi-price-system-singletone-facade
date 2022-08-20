import requests
from typing import Optional

from head.interfaces.trader.interface import ITraderComponent


class BinanceTrader(ITraderComponent):

    _endpoint = "https://api.binance.com/api/v3/ticker/price?symbol="

    @classmethod
    def getPrice(self, major: str, vs: str) -> Optional[float]:
        vs = 'usdt' if vs == 'USD' else vs
        try:
            return float(requests.get(url=self._endpoint + major.upper() + vs.upper()).json()['price'])
        except KeyError:
            return None

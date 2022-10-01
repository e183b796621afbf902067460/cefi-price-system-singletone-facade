import requests
from typing import Optional

from head.interfaces.trader.interface import ITraderComponent


class GateioTrader(ITraderComponent):

    _endpoint = "https://api.gateio.ws/api/v4/spot/tickers?currency_pair={}_{}"

    @classmethod
    def getPrice(self, major: str, vs: str, *args, **kwargs) -> Optional[float]:
        vs = 'usdt' if vs == 'USD' else vs
        try:
            return float(requests.get(url=self._endpoint.format(major.upper(), vs.upper())).json()[0]['last'])
        except KeyError:
            return None

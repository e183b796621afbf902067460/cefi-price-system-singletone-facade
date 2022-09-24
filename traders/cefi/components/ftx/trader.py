import requests
from typing import Optional

from head.interfaces.trader.interface import ITraderComponent
from head.decorators.singleton import singleton


@singleton
class FTXTrader(ITraderComponent):

    _endpoint = "https://ftx.com/api/markets/"

    @classmethod
    def getPrice(cls, major: str, vs: str = 'USD', *args, **kwargs) -> Optional[float]:
        try:
            return requests.get(url=f'{cls._endpoint}{major.upper()}/{vs.upper()}').json()['result']['price']
        except KeyError:
            return None

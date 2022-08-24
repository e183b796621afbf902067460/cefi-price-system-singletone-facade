from typing import List

from head.interfaces.trader.interface import ITraderComponent
from head.decorators.singleton import singleton
from head.decorators.yieldmethod import yieldmethod

from traders.cefi.composite.trader import cefiTrader
from traders.defi.composite.trader import defiTrader


@singleton
class HeadTrader(ITraderComponent):

    _traders: List[ITraderComponent] = list()

    def addTrader(self, trader) -> None:
        self._traders.append(trader)
        trader.setParent(parent=self)

    @yieldmethod
    def getPrice(self, major: str, vs: str = 'USD', *args, **kwargs) -> float:
        for trader in self._traders:
            yield trader.getPrice(major=major, vs=vs, *args, **kwargs)


headTrader = HeadTrader()

headTrader.addTrader(trader=cefiTrader)
headTrader.addTrader(trader=defiTrader)

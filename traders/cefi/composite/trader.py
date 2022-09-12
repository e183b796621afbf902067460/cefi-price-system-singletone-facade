from typing import List

from head.interfaces.trader.interface import ITraderComponent
from head.decorators.singleton import singleton
from head.decorators.yieldmethod import yieldmethod

from traders.cefi.components.binance.trader import BinanceTrader
from traders.cefi.components.gateio.trader import GateioTrader
from traders.cefi.components.coingecko.trader import CoingeckoTrader
from traders.cefi.components.ftx.trader import FTXTrader


@singleton
class CeFiTrader(ITraderComponent):

    _traders: List[ITraderComponent] = list()

    def addTrader(self, trader) -> None:
        self._traders.append(trader)
        trader.setParent(self, parent=self)

    @yieldmethod
    def getPrice(self, major: str, vs: str = 'USD', *args, **kwargs) -> float:
        for trader in self._traders:
            yield trader.getPrice(major=major, vs=vs, *args, **kwargs)


cefiTrader = CeFiTrader()

cefiTrader.addTrader(trader=FTXTrader)
cefiTrader.addTrader(trader=BinanceTrader)
cefiTrader.addTrader(trader=GateioTrader)
cefiTrader.addTrader(trader=CoingeckoTrader)

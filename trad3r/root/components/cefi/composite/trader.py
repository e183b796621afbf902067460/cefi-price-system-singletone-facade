from typing import Dict, Generic, Optional

from trad3r.typings.trader.typing import Trad3r
from trad3r.interfaces.trader.interface import iTrad3r
from trad3r.decorators.singleton import singleton
from trad3r.decorators.yieldmethod import yieldmethod

from trad3r.root.components.cefi.components.binance.trader import BinanceTrad3r, BinanceUSDTmTrad3r
from trad3r.root.components.cefi.components.gateio.trader import GateIOTrad3r
from trad3r.root.components.cefi.components.coingecko.trader import CoinGeckoTrad3r


@singleton
class CeFiTrad3r(iTrad3r):

    _traders: Dict[str, Trad3r] = dict()

    def add_trader(self, name: str, trader: Generic[Trad3r]) -> None:
        if not self._traders.get(name):
            self._traders[name] = trader

    def get_trader(self, name: str) -> Trad3r:
        return self._traders.get(name)

    @yieldmethod
    def get_price(self, first: str, second: str, *args, **kwargs) -> Optional[float]:
        for _, trader in self._traders.items():
            yield trader.get_price(first=first, second=second, *args, **kwargs)


ceFiTrad3r = CeFiTrad3r()

ceFiTrad3r.add_trader(name='binance', trader=BinanceTrad3r)
ceFiTrad3r.add_trader(name='gateio', trader=GateIOTrad3r)
ceFiTrad3r.add_trader(name='coingecko', trader=CoinGeckoTrad3r)
ceFiTrad3r.add_trader(name='binance_usdt_m', trader=BinanceUSDTmTrad3r)

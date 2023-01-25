from typing import List, Dict, Optional
from functools import lru_cache

from trad3r.typings.trader.typing import Trad3r
from trad3r.interfaces.trader.interface import iTrad3r
from trad3r.decorators.yieldmethod import yieldmethod
from trad3r.decorators.singleton import singleton

from trad3r.root.components.cefi.composite.trader import ceFiTrad3r


@singleton
class RootTrad3r(iTrad3r):

    _traders: Dict[str, Trad3r] = dict()

    def add_trader(self, name: str, trader: Trad3r) -> None:
        if not self._traders.get(name):
            self._traders[name] = trader

    @lru_cache
    @yieldmethod
    def get_price(
            self,
            first: str, second: str = 'USD',
            type_: str = 'cefi', source: Optional[str] = None,
            *args, **kwargs) -> Optional[float]:
        if type_ and source:
            trader: Trad3r = self._traders[type_].get_trader(name=source)
            if not trader:
                raise KeyError(f"No such Trader with type_ = {type_} and source = {source}")
            yield trader.get_price(first=first, second=second)
        else:
            for _, trader in self._traders.items():
                yield trader.get_price(first=first, second=second, *args, **kwargs)


rootTrad3r = RootTrad3r()

rootTrad3r.add_trader(name='cefi', trader=ceFiTrad3r)

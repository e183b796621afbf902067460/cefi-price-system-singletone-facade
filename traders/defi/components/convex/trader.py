from typing import Optional

from head.interfaces.trader.interface import ITraderComponent
from head.consts.chains.const import Chains
from defi.protocols.curve.contracts.Pool import CurvePoolContract
from providers.fabrics.http.fabric import httpProviderFabric


class ConvexTrader(ITraderComponent):

    _markets: dict = {
        'cvxcrvPlain3andSUSD': {
            'address': '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD',
            'provider': httpProviderFabric.getProduct(chain=Chains.ETH),
            'scale': 18
        }
    }

    @classmethod
    def getPrice(self, major: str, vs: str, *args, **kwargs) -> Optional[float]:
        try:
            market = self._markets[major]
        except KeyError:
            return None

        pool: CurvePoolContract = CurvePoolContract()\
            .setAddress(address=market['address'])\
            .setProvider(provider=market['provider'])\
            .create()
        return pool.get_virtual_price() / 10 ** market['scale']

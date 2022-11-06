from typing import Optional

from head.interfaces.trader.interface import ITraderComponent
from defi.protocols.curve.contracts.Pool import CurvePoolContract
from providers.fabrics.http.fabric import httpProviderFabric


class SturdyTrader(ITraderComponent):

    _markets: dict = {
        'cFRAX3CRV-f': {
            'address': '0xd632f22692FaC7611d2AA1C0D552930D43CAEd3B',
            'provider': httpProviderFabric.getProduct(chain='eth'),
            'scale': 18
        },
        'ccrvPlain3andSUSD': {
            'address': '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD',
            'provider': httpProviderFabric.getProduct(chain='eth'),
            'scale': 18
        },
        'cib3CRV': {
            'address': '0x2dded6Da1BF5DBdF597C45fcFaa3194e53EcfeAF',
            'provider': httpProviderFabric.getProduct(chain='eth'),
            'scale': 18
        },
        'ccrvFRAX': {
            'address': '0xDcEF968d416a41Cdac0ED8702fAC8128A64241A2',
            'provider': httpProviderFabric.getProduct(chain='eth'),
            'scale': 18
        },
        'cMIM-3LP3CRV-f': {
            'address': '0x5a6A4D54456819380173272A5E8E9B9904BdF41B',
            'provider': httpProviderFabric.getProduct(chain='eth'),
            'scale': 18
        },
        'cTUSDFRAXBP3CRV-f': {
            'address': '0x33baeDa08b8afACc4d3d07cf31d49FC1F1f3E893',
            'provider': httpProviderFabric.getProduct(chain='eth'),
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

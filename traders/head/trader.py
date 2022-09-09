from typing import List

from head.interfaces.trader.interface import ITraderComponent
from head.decorators.singleton import singleton
from head.decorators.yieldmethod import yieldmethod

from traders.cefi.composite.trader import cefiTrader
from traders.defi.composite.trader import defiTrader


@singleton
class HeadTrader(ITraderComponent):

    _traders: List[ITraderComponent] = list()
    _stablecoins: dict = {
        'eth': {
            '0x57Ab1ec28D129707052df4dF418D58a2D46d5f51': {'symbol': 'sUSD'},
            '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48': {'symbol': 'USDC'},
            '0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd': {'symbol': 'GUSD'},
            '0xdAC17F958D2ee523a2206206994597C13D831ec7': {'symbol': 'USDT'},
            '0x6B175474E89094C44Da98b954EedeAC495271d0F': {'symbol': 'DAI'},
            '0x853d955aCEf822Db058eb8505911ED77F175b99e': {'symbol': 'FRAX'},
            '0x0000000000085d4780B73119b644AE5ecd22b376': {'symbol': 'TUSD'},
            '0x4Fabb145d64652a948d72533023f6E7A623C7C53': {'symbol': 'BUSD'},
            '0x956F47F50A910163D8BF957Cf5846D573E7f87CA': {'symbol': 'FEI'},
            '0x8E870D67F660D95d5be530380D0eC0bd388289E1': {'symbol': 'USDP'},
            '0x5f98805A4E8be255a32880FDeC7F6728C6568bA0': {'symbol': 'LUSD'}
        },
        'ftm': {
            '0x049d68029688eAbF473097a2fC38ef61633A3C7A': {'symbol': 'fUSDT'},
            '0x04068DA6C83AFCFA0e13ba15A6696662335D5B75': {'symbol': 'USDC'},
            '0x82f0B8B456c1A451378467398982d4834b6829c1': {'symbol': 'MIM'},
            '0x8D11eC38a3EB5E956B052f67Da8Bdc9bef8Abf3E': {'symbol': 'DAI'},

        },
        'avax': {
            '0xc7198437980c041c805A1EDcbA50c1Ce5db95118': {'symbol': 'USDT.e'},
            '0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664': {'symbol': 'USDC.e'},
            '0xd586E7F844cEa2F87f50152665BCbc2C279D8d70': {'symbol': 'DAI.e'}
        }
    }
    _sames: dict = {
        'fUSDT': 'USDT',
        'DAI.e': 'DAI',
        'USDT.e': 'USDT',
        'USDC.e': 'USDC'
    }

    def addTrader(self, trader) -> None:
        self._traders.append(trader)
        trader.setParent(parent=self)

    @yieldmethod
    def getPrice(self, major: str, vs: str = 'USD', *args, **kwargs) -> float:
        symbol = self._same(asset=major)
        for trader in self._traders:
            yield trader.getPrice(major=symbol, vs=vs, *args, **kwargs)

    def isStablecoin(self, address: str) -> bool:
        return address in [stableAddress for addresses in self._stablecoins.values() for stableAddress in addresses]

    def _same(self, asset: str) -> str:
        return self._sames[asset] if asset in self._sames else asset


headTrader = HeadTrader()

headTrader.addTrader(trader=cefiTrader)
headTrader.addTrader(trader=defiTrader)

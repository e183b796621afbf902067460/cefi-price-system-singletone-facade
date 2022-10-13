# DeFi Traders Composite
Depends on: [defi-head-core](https://github.com/e183b796621afbf902067460/defi-head-core), [defi-contracts-evm](https://github.com/e183b796621afbf902067460/defi-contracts-evm) and [defi-providers-fabric](https://github.com/e183b796621afbf902067460/defi-providers-fabric).

---
The Trader object helps to get the price of the needed asset. The [HeadTrader](https://github.com/e183b796621afbf902067460/defi-traders-composite/blob/master/traders/head/trader.py) knows everything about every trader such as: [*CeFiTrader*](https://github.com/e183b796621afbf902067460/defi-traders-composite/blob/master/traders/cefi/composite/trader.py) and [*DeFiTrader*](https://github.com/e183b796621afbf902067460/defi-traders-composite/blob/master/traders/defi/composite/trader.py), but also each of these traders knows the sub-traders. Sub-trader returns the price value based on it market. For example, Binance can return the price of only listened assets. So, if Binance doesn't know a specific asset price an another trader may.

# Configuration
To provide needed configuration just need to set environment variables for needed blockchain node in certain [fabric](https://github.com/e183b796621afbf902067460/defi-providers-fabric/tree/master/providers/fabrics).

# Usage
Simple example:
```
from traders.head.trader import headTrader


majorCurrency = 'BTC'
vsCurrency = 'USD'

price = headTrader.getPrice(major=majorCurrency, vs=vsCurrency)
```
`getPrice()` is a [@yieldmethod](https://github.com/e183b796621afbf902067460/defi-head-core/blob/master/head/decorators/yieldmethod.py) it's means that it will recursively call `getPrice()` method from sub-traders until the price is returned.

The code above will return current BTC price in USD as underlying. 

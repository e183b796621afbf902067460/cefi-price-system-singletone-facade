# Trad3r
No dependencies.

---
The Trader object helps to get the price of the needed asset. The [RootTrad3r](https://github.com/e183b796621afbf902067460/trad3r/blob/master/trad3er/root/composite/trader.py) knows everything about every trader such as: [*CeFiTrad3r*](https://github.com/e183b796621afbf902067460/trad3r/blob/master/trad3er/root/components/cefi/composite/trader.py), but also each of these traders knows the sub-traders. Sub-trader returns the price value based on it market. For example, Binance can return the price of only listened assets. So, if Binance doesn't know a specific asset price an another trader may.

# Usage
Just base example.
```python
from trad3er.root.composite.trader import rootTrad3r


price = rootTrad3r.get_price(first='BTC')
```
`get_price()` is a [@yieldmethod](https://github.com/e183b796621afbf902067460/trad3r/blob/master/trad3er/decorators/yieldmethod.py) it's means that it will recursively call `get_price()` method from sub-traders until the price is returned.

The code above will return current BTC price in USD as underlying. 

Another usage.
```python
from trad3er.root.composite.trader import rootTrad3r


price = rootTrad3r.get_price(first='BTC', source='binance')
```
The code above will return current BTC price in USD as underlying from Binance SPOT. 

from pprint import pprint
import sys
import time
from binance import getBinance
from okx import getOkx
from kucoin import getKucoin
from bybit import getBybit
from hook import sendHook

while True:
    binanceBuy = getBinance.buy()
    binanceSell = getBinance.sell()

    okxBuy = getOkx.buy()
    okxSell = getOkx.sell()

    kucoinBuy = getKucoin.buy()
    kucoinSell = getKucoin.sell()

    bybitBuy = getBybit.buy()
    bybitSell = getBybit.sell()

    binanceBuyPrice = binanceBuy['price']
    binanceSellPrice = binanceSell['price']

    okxBuyPrice = okxBuy['price']
    okxSellPrice = okxSell['price']

    kucoinBuyPrice= kucoinBuy['price']
    kucoinSellPrice = kucoinSell['price']

    bybitBuyPrice = bybitBuy['price']
    bybitSellPrice = bybitSell['price']

    buyPrices = [ binanceBuyPrice, okxBuyPrice, kucoinBuyPrice, bybitBuyPrice ]
    sellPrices = [ binanceSellPrice, okxSellPrice, kucoinSellPrice, bybitSellPrice ]

    buy = [ binanceBuy, okxBuy, kucoinBuy, bybitBuy ]
    sell = [ binanceSell, okxSell, kucoinSell, bybitSell ]
    
    for i in range(3):
        for j in range(3):
            if sellPrices[j] - buyPrices[i] >= 1:
                sendHook(buy[i], sell[j])
                
        
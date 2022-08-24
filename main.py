from pprint import pprint
import sys
import time
from binance import getBinance
from okx import getOkx
from kucoin import getKucoin
from bybit import getBybit
from hook import sendHook, startHook

startHook()
 
lastLowestBuy = ''
lastHighestSell = ''

while True:
    binanceBuy = getBinance.buy()
    binanceSell = getBinance.sell()

    okxBuy = getOkx.buy()
    okxSell = getOkx.sell()

    #kucoinBuy = getKucoin.buy()
    #kucoinSell = getKucoin.sell()

    bybitBuy = getBybit.buy()
    bybitSell = getBybit.sell()

    binanceBuyPrice = binanceBuy['price']
    binanceSellPrice = binanceSell['price']

    okxBuyPrice = okxBuy['price']
    okxSellPrice = okxSell['price']

    #kucoinBuyPrice= kucoinBuy['price']
    #kucoinSellPrice = kucoinSell['price']

    bybitBuyPrice = bybitBuy['price']
    bybitSellPrice = bybitSell['price']

    buyPrices = [ binanceBuyPrice, okxBuyPrice, bybitBuyPrice ]
    sellPrices = [ binanceSellPrice, okxSellPrice, bybitSellPrice ]

    buy = [ binanceBuy, okxBuy, bybitBuy ]
    sell = [ binanceSell, okxSell, bybitSell ]
    
    lowestBuyPrice = 100000
    for i in range (3):
        if buyPrices[i] < lowestBuyPrice:
            lowestBuyPrice = buyPrices[i]
            lowestBuy = buy[i]
        
    highestSellPrice = 0 
    for i in range(3):
        if sellPrices[i] > highestSellPrice:
            highestSellPrice = sellPrices[i]
            highestSell = sell[i]
    
    if highestSellPrice - lowestBuyPrice >= 0:
        if (lowestBuy['userName'] != lastLowestBuy) or (highestSell['userName'] != lastHighestSell):
            sendHook(lowestBuy, highestSell)
            lastLowestBuy = lowestBuy['userName']
            lastHighestSell = highestSell['userName']
            
                
        
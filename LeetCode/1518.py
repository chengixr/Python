#1518. 换酒问题

'''
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。
'''


#使用递归
def numWaterBottles(numBottles: int, numExchange: int):
    if numBottles < numExchange:
        return numBottles
    return (numBottles - numBottles % numExchange) + \
                numWaterBottles(numBottles // numExchange + numBottles % numExchange, numExchange)
                
#循环判断
def numWaterBottles1(numBottles: int, numExchange: int):
    bottle, ans = numBottles, numBottles
    while bottle >= numExchange:
        bottle -= numExchange
        ans += 1
        bottle += 1
    return ans


if __name__ == '__main__':
    numBottles = 9
    numExchange = 3
    print(numWaterBottles(numBottles, numExchange))

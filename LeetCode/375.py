#375. 猜数字大小 II

'''
我从 1 到 n 之间选择一个数字。
你来猜我选了哪个数字。
如果你猜到正确的数字，就会 赢得游戏 。
如果你猜错了，那么我会告诉你，我选的数字比你的 更大或者更小 ，并且你需要继续猜数。
每当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。如果你花光了钱，就会 输掉游戏 。
给你一个特定的数字 n ，返回能够 确保你获胜 的最小现金数，不管我选择那个数字 。
'''

def getMoneyAmount(n):
    def test(a, b):
        if a >= b:
            return 0 
        minAmount = 9999
        #f(1, n, x) = x + max{f(1, x-1), f(x+1, n)} 取最小值
        #f(1, n) = min{f(1, n, x)} = for i in range(1, n) min{x + max{f(1, x-1), f(x+1, n)}}
        for i in range(a, b):
            result = i + max(test(a, i-1), test(i+1, b))
            minAmount = min(minAmount, result)
        return minAmount
    return test(1, n)

def getMoneyAmount1(n):
    f = [[0] * (n + 1) for _ in range(n + 1)]
    #print(f)
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
            for k in range(26):
                print(f[k])
    return f[1][n]


print(getMoneyAmount1(25))
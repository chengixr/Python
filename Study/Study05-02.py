#百鸡问题
'''
百钱百鸡是我国古代数学家[张丘建](https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)
在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
'''

import math

x = 0

for i in range(20):
    for j in range(34):
        price = (100-i-j)/3
        if price != math.floor(price):
            continue
        if (5*i + 3*j + price) == 100:
            print(i, j, 100-i-j)
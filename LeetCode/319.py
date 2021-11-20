#319. 灯泡开关
'''
初始时有 n 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭一个。

第三轮，你每三个灯泡就切换一个灯泡的开关（即，打开变关闭，关闭变打开）。第 i 轮，你每 i 个灯泡就切换一个灯泡的开关。直到第 n 轮，你只需要切换最后一个灯泡的开关。

找出并返回 n 轮后有多少个亮着的灯泡。
'''
import time
# def bulbSwitch(n:int):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1

#     sum = 0
#     if n % 2 == 0:
#         lightList = [1, 0] * int(n / 2)
#     else:
#         lightList = [1, 0] * int((n + 1) / 2)
    
#     for i in range(3, n + 1):
#         for j in range(i - 1, n, i):
#             if lightList[j] == 1:
#                 lightList[j] = 0
#             else:
#                 lightList[j] = 1
#     for i in range(len(lightList)):
#         print(i, lightList[i])
#         if lightList[i] == 1:
#             sum += 1
#     return sum

import math
def bulbSwitch(n):
    return int(math.sqrt(n))


time1 = time.time()
print(bulbSwitch(999999))
time2 = time.time()
print((time2 - time1))
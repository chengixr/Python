#找出所有水仙花数
'''
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153$
'''

import math
import time

time1 = time.time()
for i in range(153, 1000):
    sum = 0
    number = i
    while (number / 10) >= 1:
        sum = sum + math.floor(number % 10) ** 3
        number /= 10
    sum = sum + math.floor(number) ** 3
    if sum == i:
        print(i)
time2 = time.time()
print(time2 - time1)

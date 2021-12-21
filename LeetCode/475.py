#475. 供暖器

'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
'''
from typing import List
from bisect import bisect_right

def findRadius(houses: List[int], heaters: List[int]):
    ans = 0
    heaters.sort()
    for house in houses:
        j = bisect_right(heaters, house)
        i = j - 1
        rightDistance = heaters[j] - house if j < len(heaters) else float('inf')
        leftDistance = house - heaters[i] if i >= 0 else float('inf')
        curDistance = min(leftDistance, rightDistance)
        ans = max(ans, curDistance)
    return ans


houses = [1,2,3]
heaters = [2]
print(findRadius(houses, heaters))
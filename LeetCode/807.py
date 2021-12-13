#807. 保持城市天际线

'''
在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。

最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。

建筑物高度可以增加的最大总和是多少？
'''

from typing import List


def maxIncreaseKeepingSkyline(grid):
    maxRow = [0] * len(grid)
    maxLine = [0] * len(grid)
    for i in range(len(grid)):
        maxRow[i] = max(grid[i])
        for j in range(len(grid)):
            maxLine[j] = max(maxLine[j], grid[i][j])
    
    increaseHigh = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            increaseHigh += min(maxRow[i], maxLine[j]) - grid[i][j]
    return increaseHigh

#奇妙写法
def maxIncreaseKeepingSkyline1(grid):
    rowMax = list(map(max, grid))
    colMax = list(map(max, zip(*grid)))
    return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))


    
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))        
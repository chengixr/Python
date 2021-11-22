#391. 完美矩形
'''
给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
'''

def isRectangleCover(rectangles):
    sum = 0
    list1 = [] 
    for point in rectangles:
        list1 = remove(list1, point)
        sum += (point[2] - point[0]) * (point[3] - point[1])
    if len(list1) != 4:
        return False

    left, low = list1[0]
    right, up = list1[0]
    for point in list1:
        left = min(left, point[0])
        low = min(low, point[1])
        right = max(right, point[0])
        up = max(up, point[1])
    if (up - low) * (right - left) == sum:
        return True
    else:
        return False


def remove(list1, point):
    for i in (0, 2):
        for j in (1, 3):
            try:
                list1.remove([point[i], point[j]])
            except ValueError:
                list1.append([point[i], point[j]])
    return list1


rectangles = [[0, 0], [0, 1], [1, 0], [1, 1]]

print(isRectangleCover(rectangles))
    

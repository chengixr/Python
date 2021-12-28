# 825. 适龄的朋友

'''
在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
否则，x 将会向 y 发送一条好友请求。

注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

返回在该社交媒体网站上产生的好友请求总数。
'''

from typing import List
import time

# 0.5 * age[x] + 7 < age[y] <= age[x]
def numFriendRequests(ages: List[int]):
    ages.sort()
    length = len(ages)
    left, right, sum = 0, 0, 0
    for age in ages:
        if age < 15:
            continue
        while ages[left] <= 0.5 * age + 7:
            left += 1
        
        while right + 1 < length and ages[right+1] <= age:
            right += 1
        sum += right - left
    return sum


            
    
    
    
ages = [7,44,108,41,74,20,25,36,59,71,98,17,66,100,39,111,82,21,41,114,29,79,95,76,97,64,66,98,56,103,61,12,47,78,1,79,78,105,22,67,95,79,27,10,51,30,7,43,23,45,20,33,95,52,25,29,117,47,84,95,42,89,49,116,44,60,29,104,116,11,87,110]
        


print(numFriendRequests(ages))


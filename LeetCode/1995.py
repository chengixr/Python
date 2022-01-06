# 1995. 统计特殊四元组

'''
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d
'''

from typing import List


# 暴力破解
def countQuadruplets(nums: List[int]):
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        ans += 1
    return ans


# 
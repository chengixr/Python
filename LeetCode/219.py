# 219. 存在重复元素 II

"""
给你一个整数数组nums 和一个整数k ，判断数组中是否存在两个 不同的索引i和j ，
满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。
"""

from typing import List
import time


class Solution:
    @staticmethod
    def contains_near_by_duplicate(nums: List[int], k: int):
        # 暴力破解(超时)
        length = len(nums)
        for index in range(length):
            count = 1
            while count <= k and index + count < length:
                if nums[index] == nums[index + count]:
                    return True
                count += 1
        return False

    @staticmethod
    def contains_near_by_duplicate1(nums: List[int], k: int):
        # 优化：使用字典存储
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False


if __name__ == '__main__':
    num_list = [1, 2, 3, 1, 2, 3]
    set_num = 2
    solution = Solution()
    start = time.perf_counter()
    print(solution.contains_near_by_duplicate1(num_list, set_num))
    end = time.perf_counter()
    print(end - start)

    


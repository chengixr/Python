# 373. 查找和最小的K对数字

"""
给定两个以升序排列的整数数组 nums1 和 nums2,以及一个整数 k。

定义一对值(u,v)，其中第一个元素来自nums1，第二个元素来自 nums2。

请找到和最小的 k个数对(u1,v1), (u2,v2) ... (uk,vk)。
"""

from typing import List


class Solution:
    # 失败，经典超时
    # 思路是创建索引列表，长度为nums1列表长度，每个值为nums2列表中未做计算的最小值
    # 通过遍历索引列表，找到所有和的最小值，将对于的因子塞入返回列表中
    @staticmethod
    def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        length1 = len(nums1)
        length2 = len(nums2)
        count = 1       # count是标记已获取的数据数量
        index = [0] * length1       # index为索引列表
        nums = [[nums1[0], nums2[0]]]       # nums为返回列表
        if length2 == 1:        # 针对nums2只有一个数据的特殊情况
            index[0] = -1       # 索引列表中数据为-1，则代表nums1[i]与nums2中所有数据都计算过
        else:
            index[0] = 1
        # 计算出k个最小和为止
        while count < k:
            min_sum = nums1[length1 - 1] + nums2[length2 - 1] + 1       # min_sum为遍历过程中的最小和
            min_index = -1      # min_index为最小和对应的nums1列表下标
            # 遍历索引列表
            for i in range(length1):
                # 如果nums1[i]与nums2列表数据都计算过则跳过
                if index[i] == -1:
                    continue
                # 求最小和
                if min_sum > nums1[i] + nums2[index[i]]:
                    min_sum = nums1[i] + nums2[index[i]]
                    min_index = i
            nums.append([nums1[min_index], nums2[index[min_index]]])        # 最小和对应的数据塞入返回列表
            # 如果nums2列表全部计算过，则索引列表设为-1
            if index[min_index] == length2 - 1:
                index[min_index] = -1
                # 如果nums1列表最后一个数据都与nums2列表中所有数据计算过和，则说明已经全部计算，直接结束
                if index[length1 - 1] == -1:
                    return nums
            else:
                index[min_index] += 1
            count += 1
        return nums


if __name__ == '__main__':
    nums_list1 = [0, 0, 0, 0, 0]
    nums_list2 = [-3, 22, 35, 56, 76]
    k = 22
    solution = Solution()
    print(solution.k_smallest_pairs(nums_list1, nums_list2, k))

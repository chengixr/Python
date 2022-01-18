# 539. 最小时间差

"""
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
"""
from typing import List


class Solution:
    @staticmethod
    def find_min_difference(time_points: List[str]) -> int:
        # 一天24*60共1440分钟，如果给定数组长度超过1440，那一定有两个时间相同即最小时间差为0
        if len(time_points) > 1440 or len(time_points) < 2:
            return 0
        # 将所有时间转化成距离0点多少分钟，然后排序即可
        time_count = 0
        for i in range(len(time_points)):
            time_count = 600 * int(time_points[i][0]) + 60 * int(time_points[i][1]) \
                         + int(time_points[i][3:])
            time_points[i] = time_count
        time_points.sort()
        # 计算相邻数据之间的差值，找到最小值
        # 注意头尾之间也需进行比较，可能会出现00：00 23：59或相似场景
        time_count = 1440 - time_points[-1] + time_points[0]
        for i in range(1, len(time_points)):
            time_count = min(time_count, time_points[i] - time_points[i - 1])
        return time_count


if __name__ == '__main__':
    timePoints = ["00:00", "23:58", "00:04"]
    solution = Solution()
    print(solution.find_min_difference(timePoints))

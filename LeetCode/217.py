#217. 存在重复元素

'''
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 
'''


def containsDuplicate(nums):
    #使用set去重，与去重前列表长度比较
    return len(set(nums)) < len(nums)


nums = [1,2,3,4]
print(containsDuplicate(nums))
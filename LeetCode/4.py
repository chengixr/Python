# 4. 寻找两个正序数组的中位数
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。
'''


# def findMidNum(nums1:list, nums2:list):
#     numList = []
#     count1 = 0
#     count2 = 0
#     length1 = len(nums1) - 1 
#     length2 = len(nums2) - 1
#     while(count1 <= length1 and count2 <= length2):
#         if nums1[count1] < nums2[count2]:
#             numList.append(nums1[count1])
#             count1 += 1
#         elif nums1[count1] > nums2[count2]:
#             numList.append(nums2[count2])
#             count2 += 1
#         else:
#             numList.append(nums1[count1])
#             numList.append(nums2[count2])
#             count1 += 1
#             count2 += 1

#     if count1 < length1 + 1:  
#         numList += nums1[count1:]
#     else:
#         numList += nums2[count2:]

#     length = len(numList)
#     if length % 2 == 0:
#         return (numList[int(length/2-1)] + numList[int(length/2)])/2
#     else:
#         return numList[int((length-1)/2)]


def findMidNum(nums1:list, nums2:list):
    numList = []
    count1 = 0
    count2 = 0
    count = 0
    length1 = len(nums1)
    length2 = len(nums2)
    point = (length1 + length2) / 2 - 1
    while(count <= point):
        if count1 == length1:
            numList.append(nums2[count2])
            count2 += 1
            count += 1
        elif count2 == length2 or nums1[count1] < nums2[count2]:
            numList.append(nums1[count1])
            count1 += 1
            count += 1
        elif nums1[count1] > nums2[count2]:
            numList.append(nums2[count2])
            count2 += 1
            count += 1
        else:
            numList.append(nums1[count1])
            #numList.append(nums2[count2])
            count1 += 1
            #count2 += 1
            count += 1

    if count1 == length1:
        nextNum = nums2[count2]
    elif count2 == length2:
        nextNum = nums1[count1]
    else:
        nextNum = min(nums1[count1], nums2[count2])

    if (length1 + length2) % 2 == 0:
        return (numList[count-1] + nextNum) / 2
    else:
        return nextNum

nums2 = [3]
nums1 = [2,4,6,7,10,11]
print(findMidNum(nums1,nums2))

#3. 无重复字符的最长子串

'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

def lengthOfLongestSubstring(s):
    count = 0 
    sum = 0
    stringList = list(s)
    for i in range(len(stringList) + 1):
        if i == len(stringList):
            sum = max(sum, i - count)
        elif stringList[i] not in s[count:i]:
            continue
        else:
            sum = max(sum, i - count)
            count = s[count:i].index(stringList[i]) + count + 1
    return sum   


#Test



string = "   "
print(lengthOfLongestSubstring(string))







# def lengthOfLongestSubstring(s):
#     def delNum(string, list1, list2):
#         list3 = list(string)
#         for i in list3:
#             if i.isalpha():
#                 list1[ord(i)-97] = 0
#             else:
#                 list2.remove(i)
#         return list1, list2

#     if s == "":
#         return 0
#     stringList = list(s)
#     count = 0
#     sum = 0
#     number = [0]*26
#     number1 = []
#     for i in range(len(stringList)+1):
#         if i == len(stringList):
#              sum = max(sum, i - count)
#              continue
#         if stringList[i].isalpha() and number[ord(stringList[i])-97] == 1:
#             sum = max(sum, i - count)
#             point = s[count:].index(stringList[i])
#             number, number1 = delNum(s[count:point], number, number1)
#             count = point + count + 1
#             continue
#         elif stringList[i] in number1:
#             sum = max(sum, i - count)
#             point = s[count:].index(stringList[i])
#             number, number1 = delNum(s[count:point], number, number1)
#             count = point + count + 1
#             continue
        
#         if stringList[i].isalpha():
#             number[ord(stringList[i])-97] = 1
#         else:
#             number1.append(stringList[i])
#     return sum 



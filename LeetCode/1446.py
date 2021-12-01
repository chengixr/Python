#1446. 连续字符

'''
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。
'''

def maxPower(s: str):
    maxPow = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            maxPow = max(maxPow, count)
            count = 1
    return max(maxPow, count)

print(maxPower("leetcode"))
        

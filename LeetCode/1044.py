# 1044. 最长重复子串

'''
给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。
'''


def longestDupSubstring(s: str) -> str:
    ans = ""
    for i in range(len(s)):
        while(s[i:i+len(ans)+1] in s[i+1:]):
            ans = s[i:i+len(ans)+1]
    return ans


s = "banana"
print(longestDupSubstring(s))



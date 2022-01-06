# 1576. 替换所有的问号
'''
给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
'''


def modifyString(s: str):
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0 or s[i-1] == 'z':
                s = s[:i] + 'a' + s[i+1:]
            else:
                s = s[:i] + chr(ord(s[i-1]) + 1) + s[i+1:]
            if i == len(s) - 1:
                return s
            if s[i] == s[i+1]:
                if s[i] == 'z':
                    s = s[:i] + 'a' + s[i+1:]
                elif s[i] == 'a':
                    s = s[:i] + 'b' + s[i+1:]
                else:
                    s = s[:i] + chr(ord(s[i+1]) + 1) + s[i+1:]
    return s

def modifyString1(s: str):
    res = list(s)
    length = len(s)
    for i in range(length):
        if res[i] == '?':
            for b in 'abc':
                if not (i > 0 and b == res[i-1] or i < length-1 and b == res[i+1]):
                    res[i] = b
                    break
    return ''.join(res)
            
        

s = "?zs"
print(modifyString1(s))

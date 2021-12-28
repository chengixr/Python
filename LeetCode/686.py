#686. 重复叠加字符串匹配
'''
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
'''

def repeatedStringMatch(a: str, b: str):
    #count = -1
    for i in range((len(b) // len(a) + 2)):
        if b in a * i:
            #count = i
            return i
    return -1
        
    
        
    
    
    
a = "abcd"
b = "cdabcdab"
print(repeatedStringMatch(a, b))
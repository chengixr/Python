#1816. 截断句子
'''
句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。   
例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。
给你一个句子 s​​​​​​ 和一个整数 k​​​​​​ ，请你将 s​​ 截断 ​，​​​使截断后的句子仅含 前 k​​​​​​ 个单词。返回 截断 s​​​​​​ 后得到的句子。
'''

#简洁方法
def truncateSentence(s: str, k: int):
    list = s.split(" ")
    list = list[:k]
    string = " ".join(list)
    return string

#消耗内存更少
def truncateSentence1(s: str, k: int):
    n, end, count = len(s), 0, 0
    for i in range(1, n + 1):
        if i == n or s[i] == ' ':
            count += 1
            if count == k:
                end = i
                break
    return s[:end]

s = "What is the solution to this problem"
k = 4
print(truncateSentence(s, k))
print(truncateSentence1(s, k))
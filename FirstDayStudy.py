import re

print("hello world")

print(5 % 2)

# 模式匹配
# score = input("请输入")
# match score:
#     case '100':
#         print("满分")
#     case '90':
#         print("优秀")

# match函数的使用
# pattern = '\d\.\d+'
# s = "3.11第一天"
# match = re.match(pattern, s, re.I)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.string)
# print(match.group())
#
# print(re.findall(pattern, s, re.I))
#
# s1 = "python3.11、3.12学习"
# match1 = re.search(pattern, s1, re.I)
# print(match1.group())
#
# match2 = re.findall(pattern, s1, re.I)
# print(match2)

# split sub
# s1 = ('https://www.bilibili.com/video/BV1wD4y1o7AS/?p=74&spm_id_from=pageDriver&vd_source'
#       '=6e292268a8d2b78378aa82de0ede73a4')
# pattern1 = '[:|？|&]'
# lst = re.split(pattern1, s1)
# print(lst)

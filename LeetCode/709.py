#709. 转换成小写字母

'''
给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
'''

def toLowerCase(s: str):
    #简单题的天花板
    return s.lower()

def toLowerCase1(s: str):
    #将大写字母的ASCII码减小，变为对应的小写字母
    #大写字母 {A - Z} 的 ASCII 码范围为 [65, 90]
    #小写字母 {a - z} 的 ASCII 码范围为 [97, 122]
    #大写转小写可以和32使用按位或操作，小写转大写是按位或与
    
    #菜鸡写法
    string = ""
    for i in s:
        if 65 <= ord(i) <= 90:
            string += chr(ord(i) | 32)
        else:
            string += i
    return string

    #高手写法
    #return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)



s = "Hello"
print(toLowerCase1(s))
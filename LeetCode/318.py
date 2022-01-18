# 318. 最大单词长度乘积


def maxProduct(words):
    product = 0
    length = len(words)
    mask = [[0]*26 for i in range(length)]
    for i in range(length):
        for oled in words[i]:
            mask[i][ord(oled) - 97] = 1
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            index = False
            for oled in range(26):
                if mask[i][oled] & mask[j][oled] == 1:
                    index = True
                    break
            if index == False:
                product = max(product, len(words[i]) * len(words[j]))
        
    return product

words = ["a","aa","aaa","aaaa"]
print(maxProduct(words))

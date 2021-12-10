#748. 最短补全词

'''
给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出并返回 words 中的 最短补全词 。

补全词 是一个包含 licensePlate 中所有的字母的单词。在所有补全词中，最短的那个就是 最短补全词 。

在匹配 licensePlate 中的字母时：

忽略 licensePlate 中的 数字和空格 。
不区分大小写。
如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。

请你找出并返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 最靠前的 那个。
'''



from typing import List


def shortestCompletingWord(licensePlate: str, words: List[str]):
    licenseDict = {}
    completingWord = ''
    for i in licensePlate:
        if not i.isalpha():
            continue
        i = i.lower()
        if i in licenseDict:
            licenseDict[i] += 1
        else:
            licenseDict[i] = 1
    
    for i in words:
        i = i.lower()
        boolDict = True
        for key in licenseDict.keys():
            if licenseDict[key] > i.count(key):
                boolDict = False
                break
        if boolDict == False:
            continue         
        if len(completingWord) > len(i) or completingWord == '':
            completingWord = i
    return completingWord
        
    
    
if __name__ == '__main__':
    licensePlate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    print(shortestCompletingWord(licensePlate, words))
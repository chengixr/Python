#859. 亲密字符串

'''
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
'''


def buddyStrings(s, goal):
    count = 0
    countList = [0] * 26
    acountList = []
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        if s[i] != goal[i]:
            acountList.append(s[i])
            acountList.append(goal[i])
            count += 1
        countList[ord(s[i]) - 97] += 1
    
    acount = False
    for i in range(26):
        if countList[i] >= 2:
            acount = True
            break
    
    if count == 2 and acountList[0] == acountList[3] and acountList[1] == acountList[2]:
        return True
    elif count == 0 and acount == True:
        return True
    else:
        return False

s = "aaaaaaabc"
goal = "aaaaaaacb"
print(buddyStrings(s, goal))
#423. 从英文中重建数字

'''
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。
'''

'''
zero    z
one     o - z - w - u
two     w
three   h - g
four    u
five    f - u
six     x
seven   v - f + u
eight   g
nine    i - g - x - f + u
'''

def originalDigits(s:str):
    numString = ""
    
    countZero = s.count('z')
    countTwo = s.count('w')   
    countFour = s.count('u')
    countSix = s.count('x')
    countEight = s.count('g')
    countOne = s.count('o') - countZero - countTwo - countFour
    countThree = s.count('h') - countEight
    countFive = s.count('f') - countFour
    countSeven = s.count('v') - countFive
    countNine = s.count('i') - countFive- countSix - countEight

    # countNum = [countZero, countOne, countTwo, countThree, countFour, 
    #             countFive, countSix, countSeven,countEight, countNine]
    #固定数据可使用元组
    countNum = (countZero, countOne, countTwo, countThree, countFour, 
                countFive, countSix, countSeven,countEight, countNine)

    for i in range(len(countNum)):
        numString = numString + str(i) * countNum[i]
    
    return numString

s = "owoztneoer"
print(originalDigits(s))



    

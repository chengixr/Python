#找出10000以内的**完美数**

import math

def findPerfectName():
    for number in range(1, 100):
        sum = 1
        for factor in range(2, int(math.sqrt(number))+1):
            if number % factor == 0:
                if factor==number/factor:
                    sum += factor
                else:
                    sum = sum + factor + number/factor

        #if sum == number:
        #    print(number)
        if sum == 1:
            print(number) 

if __name__ == '__main__':
    findPerfectName()
'''
    for num in range(1, 10000):
        result = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                if factor > 1 and num // factor != factor:
                    result += num // factor
            if result == num:
                print(num)
'''
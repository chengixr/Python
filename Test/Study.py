from math import fabs
import os
import time
import random

# def main():
#     num = int(input("Number of rows:"))
#     yh = [[]] * num
#     for row in range(num):
#         yh[row] = [None] * (row + 1)
#         for col in range(row+1):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row-1][col-1] + yh[row-1][col]
#             print(yh[row][col], end='\t')
#         print()


class Clock():
    def __init__(self, hour=0, minute=0, second=0):
        self._second = second
        self._minute = minute
        self._hour = hour

    @staticmethod
    def is_clock(hour, minute, second):
        if hour < 0 or hour >= 24 or minute < 0 or minute >=60 or second < 0 or second >= 60:
            return False
        else:
            return True
    
    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
        
    def show(self):
        print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))

def main(hour, minute, second):
    #hour, minute, second = 23, 59, 40
    if Clock.is_clock(hour, minute, second):
        clock = Clock(hour, minute, second)
        while True:
            os.system('cls')
            clock.show()
            time.sleep(1)
            clock.run()
    else:
        print("非法输入")


if __name__ == '__main__':
    main(23 , 59, 50)
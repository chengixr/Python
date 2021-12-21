#1154. 一年中的第几天

'''
给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
'''

def dayOfYear(date: str):
    year, month, day = date.split('-')
    year, month, day = int(year), int(month), int(day)
    
    #year, month, day = [int(x) for x in date.split("-")]
    
    colum = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        colum[1] += 1
    
    return sum(colum[:month-1]) + day

date = "2004-03-01"
print(dayOfYear(date))



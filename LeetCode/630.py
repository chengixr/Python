#630. 课程表 III

'''
这里有 n 门不同的在线课程，按从 1 到 n 编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi] 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。

你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。
'''


from typing import List

#菜鸡写法

def scheduleCourse(courses: List):
    # 总花费时间
    sumCourseCost = 0
    # 准备学习序列
    studyCourses = []
    
    # 先按截止时间排序
    courses.sort(key=(lambda x: x[1]))
 
    for course in courses:
        # 如果准备学习的课程加上当前课程的花费时间，小于当前课程的截止时间
        # 可以将当前课程加入准备学习课程中
        if sumCourseCost + course[0] <= course[1]:
            studyCourses.append(course)
            sumCourseCost += course[0]
        else:
            # 花费时间最大值，默认为当前课程花费时间
            maxCost = course[0]
            # 花费时间最大数据的序列，默认为-1
            index = -1
            # 遍历准备学习课程，找到花费时间最大值
            for i in range(len(studyCourses)):
                if studyCourses[i][0] >= maxCost:
                    maxCost = studyCourses[i][0]
                    index = i
            # 如果最大值是当前课程，跳过
            if index == -1:
                continue
            # 将花费时间最大的抛出，将当前课程插入
            else:                  
                sumCourseCost += course[0] - studyCourses[index][0]
                studyCourses.pop(index)
                studyCourses.append(course)
                
    return len(studyCourses)


import heapq
#高手写法
def scheduleCourse1(courses: List):
    courses.sort(key=lambda c: c[1])

    q = list()
    # 优先队列中所有课程的总时间
    total = 0

    for ti, di in courses:
        if total + ti <= di:
            total += ti
            # Python 默认是小根堆
            heapq.heappush(q, -ti)
        elif q and -q[0] > ti:
            total -= -q[0] - ti
            heapq.heappop(q)
            heapq.heappush(q, -ti)

    return len(q)


    
courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
print(scheduleCourse(courses))
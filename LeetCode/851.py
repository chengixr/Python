#851. 喧闹和富有

'''
有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。

给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。
richer 中所给出的数据 逻辑自恰（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。

现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人（也就是安静值 quiet[y] 最小的人）。
'''

from typing import List



def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    richerList = []
    peopleList = [-1] * len(quiet)
    for i in range(len(quiet)):
        richerList.append(richerPeople(richer, quiet, peopleList, i))
    return richerList 
    
def richerPeople(richer: List[List[int]], quiet: List[int], peopleList: List[int], people) -> int:
    if peopleList[people] != -1:
        return quiet.index(peopleList[people])
    minLoud = quiet[people]
    for i in range(len(richer)):
        if richer[i][1] == people:
            # boolIndex = i
            minLoud = min(quiet[richerPeople(richer, quiet, peopleList, richer[i][0])], minLoud)
            
    # if boolIndex == -1:
    #     minLoud = quiet[people]
    peopleList[people] = minLoud
    return quiet.index(minLoud)
            

#高手写法，深度优先搜索            
def loudAndRich1(richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    g = [[] for _ in range(n)]
    for r in richer:
        g[r[1]].append(r[0])

    ans = [-1] * n
    def dfs(x: int):
        if ans[x] != -1:
            return
        ans[x] = x
        for y in g[x]:
            dfs(y)
            if quiet[ans[y]] < quiet[ans[x]]:
                ans[x] = ans[y]
    for i in range(n):
        dfs(i)
    return ans


        
    
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(loudAndRich(richer, quiet))
        
            
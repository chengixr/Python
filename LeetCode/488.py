#488.祖玛游戏

'''
你正在参与祖玛游戏的一个变种。

在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。

你的目标是 清空 桌面上所有的球。每一回合：

从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
如果桌面上所有球都被移除，则认为你赢得本场游戏。
重复这个过程，直到你赢了游戏或者手中没有更多的球。
给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。
'''


'''
def findMinStep(board: str, hand: str) -> int:
        def remove(b):
            i = 0
            for j in range(len(b)+1):
                if j == len(b) or b[j] != b[i]:
                    if j - i >= 3:
                        return remove(b[:i]+b[j:])
                    i = j
            return b
        
        #@lru_cache(None)
        def dfs(b, h):
            b = remove(b)
            if b and not h: 
                return float('inf')
            if not b: 
                return 0
            
            res = float('inf')
            for i in range(1, max(len(b)-1,2)):
                for j in range(len(h)):
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res
        
        hand = ''.join(filter(lambda x: x in board, hand))
        res = dfs(board, hand)
        return res if res != float('inf') else -1


board = "RBYYBBRRB"
hand = "YRBGB"
print(findMinStep(board, hand))

'''
import re
from typing import Deque



class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            # 消除桌面上需要消除的球
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        hand = "".join(sorted(hand))

        # 初始化用队列维护的状态队列：其中的三个元素分别为桌面球状态、手中球状态和回合数
        queue = Deque([(board, hand, 0)])

        # 初始化用哈希集合维护的已访问过的状态
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # 第 1 个剪枝条件: 当前球的颜色和上一个球的颜色相同
                if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                    continue

                # 第 2 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球
                if i > 0 and cur_board[i - 1] == cur_hand[j]:
                    continue

                # 第 3 个剪枝条件: 只在以下两种情况放置新球
                #  - 第 1 种情况 : 当前球颜色与后面的球的颜色相同
                #  - 第 2 种情况 : 当前后颜色相同且与当前颜色不同时候放置球      
                choose = False
                if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                    choose = True
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    choose = True

                if choose:
                    new_board = clean(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    if not new_board:
                        return step + 1
                    if (new_board, new_hand) not in visited:
                        queue.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))

        return -1

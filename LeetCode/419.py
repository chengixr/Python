#419. 甲板上的战舰

'''
给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，
返回在甲板 board 上放置的 战舰 的数量。

战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，
其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。
'''


from typing import List

def countBattleships(board: List[List[str]]):
    # 遍历整个二维列表，找到战舰头，即左方上方都为空的'X'
    # 注意第一列和第一行单独判断
    shipsCount = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                shipsCount += 1
    return shipsCount
            # if board[i][j] != 'X':
            #     continue
            # if i == 0:
            #     if j == 0:
            #         shipsCount += 1
            #         continue
            #     elif board[i][j - 1] == ".":
            #         shipsCount += 1
            #         continue
            # elif j == 0:
            #     if board[i - 1][j] == '.':
            #         shipsCount += 1
            #         continue
            # elif board[i - 1][j] == '.' and board[i][j - 1] == '.':
            #     shipsCount += 1
            #     continue
    # return shipsCount


def countBattleships1(board: List[List[str]]):
    shipsCount = 0
    m, n = len(board), len(board[0])
    for i, row in enumerate(board):
        for j, ch in enumerate(row):
            if ch == 'X':
                for k in range(i + 1, m):
                    if board[k][j] == 'X':
                        board[k][j] = '.'
                    else:
                        break
                for l in range(j + 1, n):
                    if board[i][l] == 'X':
                        board[i][l] = '.'
                    else:
                        break
                shipsCount += 1
    return shipsCount


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(countBattleships1(board))
#794. 有效的井字游戏

'''
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
'''



def validTicTacToe(board):    
    #如果超过三行，不符合规则
    if len(board) != 3:
        return False
    countX, countO = 0, 0
    for i in range(3):
        #如果一行超过3个字符，不符合规则
        if len(board[i]) >= 4:
            return False
        countO += board[i].count('O')
        countX += board[i].count('X')
        while(len(board[i]) < 3):
            board[i] = board[i] + " "
        
    
    #如果先手棋子数小于后手 或 大于后手两个或以上，不符合规则
    if countX < countO or countX > countO + 1:
        return False
    
    winner = ''
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            winner += board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            winner += board[0][i]
            
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner += board[1][1]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        winner += board[1][1]
    
    if len(winner) > 1 and winner[0] != winner[1]:
        return False
    elif winner[0] == 'X' and countX == countO:
        return False
    elif len(winner) == 1 and winner[0] == 'O' and countX != countO:
        return False
    
    return True
        
            
    
'''
def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
                   board[0][0] == p and board[1][1] == p and board[2][2] == p or \
                   board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        oCount = sum(row.count('O') for row in board)
        xCount = sum(row.count('X') for row in board)
        return not (oCount != xCount and oCount != xCount - 1 or
                    oCount != xCount and self.win(board, 'O') or
                    oCount != xCount - 1 and self.win(board, 'X'))
'''

    
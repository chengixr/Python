theBoard = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ', 'mid_L': ' ', 'mid_M': ' ',
            'mid_R': ' ', 'low_L': ' ', 'low_M': ' ', 'low_R': ' '}

def printBoard(board):
    print(' ' + board['top_L'] + ' | ' + board['top_M'] + ' | ' + board['top_R'])
    print('---+---+---')
    print(' ' + board['mid_L'] + ' | ' + board['mid_M'] + ' | ' + board['mid_R'])
    print('---+---+---')
    print(' ' + board['low_L'] + ' | ' + board['low_M'] + ' | ' + board['low_R'])

def checkVictory(board):
    arrLeft = ['top', 'mid', 'low']
    arrRight = ['L', 'M', 'R']
    for i in arrLeft:
        arr = []
        count = 0
        for j in arrRight: 
            arr.append(board[i + '_' + j])
            count += 1
        if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] != ' ':
            return arr[0]
    
    for j in arrRight:
        arr = []
        count = 0
        for i in arrLeft:
            arr.append(board[i + '_' + j])
            count += 1
        if arr[0] == arr[1] and arr[1] == arr[2] and arr[0] != ' ':
            return arr[0]
    return 'null'


turn = 'X'
count = 0
while(checkVictory(theBoard) == 'null'):
    print('Turn for ' + turn + ' Move on the board')
    move = input()
    theBoard[move] = turn
    printBoard(theBoard)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    count += 1
    if count == 9:
        print('This game is no winner.')
print('Winner is ' + checkVictory(theBoard) + '!')


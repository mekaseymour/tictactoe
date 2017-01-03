theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    #gameWin(theBoard, turn)

    if ((theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn) or
    (theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn) or
    (theBoard['low-L'] == turn and theBoard['low-M'] == turn and theBoard['low-R'] == turn) or
    (theBoard['top-L'] == turn and theBoard['mid-L'] == turn and theBoard['low-L'] == turn) or
    (theBoard['top-M'] == turn and theBoard['mid-M'] == turn and theBoard['low-M'] == turn) or
    (theBoard['top-R'] == turn and theBoard['mid-R'] == turn and theBoard['low-R'] == turn) or
    (theBoard['top-L'] == turn and theBoard['mid-M'] == turn and theBoard['low-R'] == turn) or # wins diagonally
    (theBoard['top-R'] == turn and theBoard['mid-M'] == turn and theBoard['low-L'] == turn)):
        print ("\nPlayer %s wins!!!!\n" % turn)
        break
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


#printBoard(theBoard)

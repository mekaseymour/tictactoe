# Simple tic tac toe logic and board

theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def playGame():
    player = input("Which player would you like to be (X or O)?")
    turn = player.upper()

    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = int(input())
        theBoard[move] = turn
        #gameWin(theBoard, turn)

        if ((theBoard[1] == turn and theBoard[2] == turn and theBoard[3] == turn) or # wins across the top
        (theBoard[4] == turn and theBoard[5] == turn and theBoard[6] == turn) or # wins across the middle row
        (theBoard[7] == turn and theBoard[8] == turn and theBoard[9] == turn) or # wins across the bottom
        (theBoard[1] == turn and theBoard[4] == turn and theBoard[7] == turn) or # wins down the left column
        (theBoard[2] == turn and theBoard[5] == turn and theBoard[8] == turn) or # wins down the middle column
        (theBoard[3] == turn and theBoard[6] == turn and theBoard[9] == turn) or # wins down the right column
        (theBoard[1] == turn and theBoard[5] == turn and theBoard[9] == turn) or # wins diagonally
        (theBoard[3] == turn and theBoard[5] == turn and theBoard[7] == turn)): # wins diagonally
            print ("\nPlayer %s wins!!!!\n" % turn)
            break
        else:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

playGame()

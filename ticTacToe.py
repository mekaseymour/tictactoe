# Simple tic tac toe logic and board
from random import randint

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
    # ask user to choose to be player 'X' or 'O'
    player_one = input("Which player would you like to be (X or O)?: ")
    player_one = player_one.upper()

    # check that the user's entry is either 'X' or 'O'
    while player_one != 'X' and player_one != 'O':
        player_one = input("Enter either X or O to start.: ")
        player_one = player_one.upper()

    print("OK! Let's play!\n")
    printBoard(theBoard)

    # randomly pick which player goes first
    choice = randint(1,2)
    if choice == 1:
        turn = 'X'
    else:
        turn = 'O'

    for i in range(9):
        #print('Turn for ' + turn + '. Move on which space?')
        print('Turn for ' + turn + '.')
        if turn != player_one:
            # computer plays
            computer_pick = randint(1,9)
            # picks new random position if that board space already contains an 'X' or 'O'
            while theBoard[computer_pick] != ' ':
                computer_pick = randint(1,9)
            theBoard[computer_pick] = turn
        else:
            # user plays
            print('Move on which space?')
            move = int(input())
            # re-promppts user if that board space already contains an 'X' or 'O'
            while theBoard[move] != ' ':
                move = int(input('Choose an empty space (1-9): '))
            theBoard[move] = turn

        printBoard(theBoard)

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
            # if no one has won yet, switch turns
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

playGame()

'''
Step 1: Write a function that can print out a board. 
Set up your board as a list, where each index 1-9 corresponds 
with a number on a number pad, so you get a 3 by 3 board representation.
'''
# Useful only for Clear screen in Jupyter
from IPython.display import clear_output 
import random
import sys
import os

## os.system("clear")  # Clear screen..."cls" works too
# Useful to clear screen on all platforms in VSC

def display_board(board):
    os.system("clear")
    # clear_output() 
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | '  + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | '  + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | '  + board[3])
    print('   |   |')
## Test board...
test_board = ['#','x','o','x','o','x','o','x','o','x']
#display_board(test_board)

'''
Step 2: Write a function that can take in a player input 
and assign their marker as 'X' or 'O'. Think about using 
while loops to continually ask until you get a correct answer.
'''
def player_input():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            return ('x', 'o')
        else:
            return ('o', 'x')

## Test Step 2 is taking Input successfully
#print(player_input())


'''
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, marker, position):
    board[position] = marker

## Test Step 3: run the place marker function using test parameters and display
## the modified  board
#place_marker(test_board, '$', 8)
#display_board(test_board)

''' 
Step 4: Write a function that takes in a board and checks to see 
if someone has won.
'''
def win_check(board, mark):

    return (
    # across the top
    (board[7] == mark and board[8] == mark and board[9] == mark)
    # or across the middle
    or (board[4] == mark and board[5] == mark and board[6] == mark)
    # or across the bottom
    or (board[1] == mark and board[2] == mark and board[3] == mark)
    # or down the middle
    or (board[7] == mark and board[4] == mark and board[1] == mark)
    # or down the middle
    or (board[8] == mark and board[5] == mark and board[2] == mark)
    # or down the right side
    or (board[9] == mark and board[6] == mark and board[3] == mark)
    # or diagonal
    or (board[7] == mark and board[5] == mark and board[3] == mark)
    # or diagonal
    or (board[9] == mark and board[5] == mark and board[1] == mark)
    )
## Run the win_check() against our test_board. It should return True
## print(win_check(test_board, 'x'))

'''
Step 5: Write a function that uses the random module to randomly decide 
which player goes first. You may want to lookup random.randint()
Returns a string of which player went first 
'''
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

'''
Step 6: Write a function that returns a boolean indicating wheter a space 
on the board is frrly available
'''
def space_check(board, position):
    return board[position] == ' '

'''
Step 7: Write a function that checks if the board is full and returns a boolean value if full, 
False otherwise
'''
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

'''
Step 8: Write a function that asks for a player's position (as a number 1-9)
and then uses the function from Step 6 to check if it's a free position. 
If it is, then return the position for later use
'''
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

        return position

'''
Step 9: Write a funtion that asks the player if they want to play again
and returns a boolean True if they do want to play again
'''
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

'''
Step 10: Use while loop and the functions created in this program to run the game!
'''
print('Welcome to Tic Tac Toe')
while True:
    #Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to play? Enter Yes(y) or No(n): ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! you have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2. You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


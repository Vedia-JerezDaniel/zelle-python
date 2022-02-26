# Tic-Tac-Toe Program using
# random number in Python

from math import e
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
	return(np.array([[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]]))

# Check for empty places on board
def possibilities(board):  # sourcery skip: for-append-to-extend
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return(l)

# Select a random place for the player
def random_place(board, player):
	selection = possibilities(board)
	current_loc = random.choice(selection)
	board[current_loc] = player
	return(board)

# Checks whether the player has three of their marks in a horizontal row
def row_win(board, player):
	for x in range(len(board)):
		win = all(board[x, y] == player for y in range(len(board)))
		if win:
			return(win)
	return(win)

# Checks whether the player has three of their marks in a vertical row
def col_win(board, player):
	for x in range(len(board)):
		win = all(board[y][x] == player for y in range(len(board)))
		if win:
			return(win)
	return(win)

# Checks whether the player has three of their marks in a diagonal row
def diag_win(board, player):
	y = 0
	win = all(board[x, x] == player for x in range(len(board)))
	if win:
	    return win
	win = True
	if win:
	    for x in range(len(board)):
	        y = len(board) - 1 - x
	        if board[x, y] != player:
	            win = False
	return win

# Evaluates whether there is a winner or a tie
def evaluate(board):
	winner = 0
	for player in [1, 2]:
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)):
			winner = player
			
	if np.all(board != 0) and winner == 0:
		winner = -1
	return winner

# Main function to start the game
def play_game():
	board, winner, counter = create_board(), 0, 1
	print(board)
	sleep(3)

	while winner == 0:
		for player in [1, 2]:
			board = random_place(board, player)
			print(f"Board after {counter} move")
			print(board)
			sleep(3)
			counter += 1
			winner = evaluate(board)
			if winner != 0:
				break
	return(winner)

# Driver Code
print(f"Winner is: {str(play_game())}")


# ---------------------------------
def fun(insi =2, o=3):
    return insi * o

print(fun(3))

tup = (1,) + (1, )
tup = tup + tup
len(tup)


try:
    fp = input("endt 1")
    a = len(fp)
    se = input("endt 2")
    b = len(se) * 2
    print(a/b)
except ZeroDivisionError:
    print("no zero")
except ValueError:
    print("wrongf al")
except:
    print("eororor")



val = input("enter a val value: ")
print(10/val)
from tkinter import *
from turtle import pos

# tic tac toe grid and numeration

#   1 | 2 | 3
#---------------
#   4 | 5 | 6
#---------------
#   7 | 8 | 9

"""
We need to check after each move if X or O won the game.
There are 8 possible ways in which one can tic tac toe:

SN1       SN2       SN3     SN4     SN5     SN6     SN7     SN8

A--       -A-       --A     AAA     ---     ---     A--     --A
A--       -A-       --A     ---     AAA     ---     -A-     -A-
A--       -A-       --A     ---     ---     AAA     --A     A--
"""

#----------------------- Global variables -----------------------

#player and computer current_chrs
player = 'O'
computer = 'X'

#empty grid
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
#----------------------------------------------------------------

def print_board(board):
    print("\n")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3] + "\t" + " 1 | 2 | 3")
    print("---------" + "\t" + "-----------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6] + "\t" + " 4 | 5 | 6")
    print("---------" + "\t" + "-----------")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9] + "\t" + " 7 | 8 | 9")
    print("\n")

print_board(board)

#----------- Position Checking and Inserting New Moves to Board ----------- 
# checks selected position
def is_empty(position):
    if(board[position] == ' '):
        return True
    else:
        return False

# inserting moves to board
def insert_pos(current_chr, position):
    
    if is_empty(position):
        board[position] = current_chr
        print_board(board)
        
        if(check_draw()):
            print("Its draw!!")
            exit()
            
        if(check_win()):
            if current_chr == 'X':
                print("Computer won!!")
                exit()
        
            # never going to happen lol
            else:
                print("Player won!!")
                exit() 
        return
    else:
        print("Can't insert that position!")
        position = int(input("Enter new position: "))
        insert_pos(current_chr, position)
#-----------------------------------------------------------------------

#----------------------- Win or Draw Scenarios -----------------------
def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):     # sn4
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):   # sn5
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):   # sn6
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):   # sn1
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):   # sn2
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):   # sn3
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):   # sn7
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):   # sn8
        return True
    else:
        return False
    
# for calculating minimax max and min scores
def calculate_Scores_minimax(current_chr):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == current_chr):     # sn4
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == current_chr):   # sn5
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == current_chr):   # sn6
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == current_chr):   # sn1
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == current_chr):   # sn2
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == current_chr):   # sn3
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == current_chr):   # sn7
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == current_chr):   # sn8
        return True
    else:
        return False
           
# if there are empty spaces we can still play otherwise its draw
def check_draw():
    for key in board.keys():
        if( board[key] == ' '):
            return False
    return True
#------------------------------------------------------------------  

#------------------- Ai and Player moves -------------------
def player_move():
    position = int(input("Enter the position for 'O': "))
    insert_pos(player, position)
    return

def computer_move():
    
    #Maximizing 
    best_Score = -1000
    best_Move = 0
    
    #moving on each possible key
    for Key in board.keys():
        if(board[Key] == ' '):
            board[Key] = computer
            #calculating best score for each empty point in board
            score = minimax_alg(board, 0, False)
            board[Key] = ' '
            if(score > best_Score):
                best_Score = score
                best_Move = Key
                
    insert_pos(computer, best_Move)
    return
#-----------------------------------------------------------

#------------------- Minimax Algorithm -------------------
def minimax_alg(board, depth, isMaximizing):
    #stopping conditions and who is winning
    if calculate_Scores_minimax(computer):
        return 100
    elif calculate_Scores_minimax(player):
        return -100
    elif check_draw():
        return 0
    
    if isMaximizing:
        best_Score = -1000
        
        #moving on each possible key
        for Key in board.keys():
            if(board[Key] == ' '):
                board[Key] = computer
                #calculating best score for each empty point in board
                score = minimax_alg(board, 0, False)
                board[Key] = ' '
                if(score > best_Score):
                    best_Score = score
                    best_Move = Key
        return best_Score
    
    else:
        #Minimizing
        best_Score = 1000
        
        for Key in board.keys():
            if(board[Key] == ' '):
                board[Key] = player
                score = minimax_alg(board, depth + 1, True)
                board[Key] = ' '
                if(score < best_Score):
                    best_Score = score
        return best_Score
#-----------------------------------------------------------
while not check_win():
    computer_move()
    player_move()
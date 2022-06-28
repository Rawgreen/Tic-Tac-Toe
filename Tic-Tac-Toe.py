import tkinter as tk

#----------------------- Global variables -----------------------
root = tk.Tk()
current_chr = "X"
player_points = []
comp_points = []
XO_points = []
#----------------------------------------------------------------

        
#----------------------- Window settings ------------------------
root.resizable(False, False)
root.title("My Tic Tac Toe Game with Minimax Algorithm")

#.pack() is a geometry manager which organizes widgets in blocks before placing them in the parent widget
tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

# for printing turns and current status
status_label = tk.Label(root, text = "Player's turn", font = ('Ariel', 15), bg = 'green', fg = 'snow')
status_label.pack(fill =tk.X)

def play_again():
    global current_chr
    current_chr = 'X'
    for point in XO_points:
        point.button.configure(state = tk.NORMAL)
        point.reset()
    status_label.configure(text = "Player's turn")
    play_again_button.pack_forget()
play_again_button = tk.Button(root, text = "Play again", font =('Ariel', 15), command = play_again)

play_area = tk.Frame(root, width = 500, height = 500, bg ='white')

# creating empty array for buttons
XO_points = []
#----------------------------------------------------------------

#----------------------- Grid Settings and Basic Operations ------------------------
class XO_Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None   # null
        self.button = tk.Button(play_area, text = "", width = 20, height = 10, command = self.set)
        # .grid() same as .pack() but used for organizing widgets in a table like structure in the parent widget
        self.button.grid(row = x, column = y)
       
    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text = current_chr, bg = 'snow', fg = 'black')
            self.value = current_chr
            if current_chr == "X":
                player_points.append(self)
                current_chr = "O"
                status_label.configure(text = "Computer's turn")
            elif current_chr == "O":
                comp_points.append(self)
                current_chr = "X"
                status_label.configure(text = "Player's turn")
        check_win()
    
    def reset(self):
        #.configure() can be used on any widget to change settings that you may have applied earlier, or haven't applied yet
        self.button.configure(text = "", bg = 'lightgray')
        if self.value == "X":
            player_points.remove(self)
        elif self.value == "O":
            comp_points.remove(self)
        self.value = None
        
        
for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XO_Point(x, y))
#----------------------------------------------------------------

#----------------------- Winning Logic ------------------------
"""
We need to check after each move if X or O won the game.
There are 8 possible ways in which one can tic tac toe:

SN1       SN2       SN3     SN4     SN5     SN6     SN7     SN8

A--       -A-       --A     AAA     ---     ---     A--     --A
A--       -A-       --A     ---     AAA     ---     -A-     -A-
A--       -A-       --A     ---     ---     AAA     --A     A--
"""

class WinningLogic:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, for_chr):
        # we need 3 consecutive symbols to win
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        
        if for_chr == "X":
            for point in player_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == "O":
            for point in comp_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
                    
        #all() function returns true if all items in an iterable are true, otherwise it returns false.
        return all([p1_satisfied, p2_satisfied, p3_satisfied])
#----------------------------------------------------------------

# Creating new objects which holds each condition to win (Line 80)
winning_possibilities = [
    WinningLogic(1, 1, 2, 1, 3, 1),     # sn1
    WinningLogic(1, 2, 2, 2, 3, 2),     # sn2
    WinningLogic(1, 3, 2, 3, 3, 3),     # sn3
    WinningLogic(1, 1, 1, 2, 1, 3),     # sn4
    WinningLogic(2, 1, 2, 2, 2, 3),     # sn5         
    WinningLogic(3, 1, 3, 2, 3, 3),     # sn6
    WinningLogic(1, 1, 2, 2, 3, 3),     # sn7
    WinningLogic(3, 1, 2, 2, 1, 3)      # sn8
    ]

#-------------------------- Disabling Grid --------------------------
# Disasbles interaction with grid after one of the 8 conditions has been met
def disable_game():
    for point in XO_points:
        point.button.configure(state = tk.DISABLED)
    play_again_button.pack()
#---------------------------------------------------------------------

#-------------------------- Checking Each Player --------------------------
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('X'):
            status_label.configure(text = "Player won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text = "Computer won!")
            disable_game()
            return
    if len(player_points) + len(comp_points) == 9:
        status_label.configure(text = "Draw!")
        disable_game()
#--------------------------------------------------------------------------

play_area.pack(padx = 10, pady = 10)
root.mainloop()
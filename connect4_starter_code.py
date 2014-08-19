# GROUP MEMBERS:
# 
# 
# 
# 


# FILL IN THE FUNCTIONS BELOW
# IN EACH FUNCTION, WRITE WHO WORKED ON IT
# IN EACH FUNCTION, WRITE THE PARAMETERS (INPUTS)


# DO NOT CHANGE THE NEXT 4 LINES
import turtle
turtle.penup()
turtle.hideturtle()
turtle.tracer(0, 0)

# variables that set up the game
# CHANGE THESE AS NEEDED
BOARD_HEIGHT = 6
BOARD_WIDTH = 7
START_X = -175
START_Y = 125
CELL_SIZE = 50 # side length of the square
PLAYER1 = 'red'
PLAYER2 = 'blue'
BASE_COLOR = 'black'
board = [[0,1,2,3,4,5],
         [0,1,2,3,4,5],
         [0,1,2,3,4,5],
         [0,1,2,3,4,5],
         [0,1,2,3,4,5],
         [0,1,2,3,4,5],
         [0,1,2,3,4,5]]
cur_player = 1


# MADE BY: 
# draws a vertical line on the screen
# It should start at (x, y) and be of size length
def vert_line():
    pass

# MADE BY:
# draws a horizontal line on the screen
# It should start at (x, y) and be of size length
def horiz_line():
    pass

# MADE BY:
# draw the entire game board using the vert_line
# and horiz_line functions starting at (x, y)
def draw_board():
    pass

# MADE BY:
# input the column number, row number, and piece color
# and draw a circular game piece
def draw_piece():
    pass

# MADE BY:
# check for a win (4 pieces of the same color) in a column
def check_down():
    return False

# MADE BY:
# check for a win (4 pieces of the same color) in a row
def check_row():
    return False

# MADE BY:
# check for a win (4 pieces of the same color) in the
# diagonal from the bottom left to the top right
def check_main_diagonal():
    return False

# MADE BY:
# check for a win (4 pieces of the same color) in the
# diagonal from the top left to the bottom right
def check_sub_diagonal():
    return False

# MADE BY:
# use the check_down, check_row, check_main_diagonal,
# and check_sub_diagonal functions to check the board
# for a win
# Hint: make sure you input the row and column
def check_for_win():
    pass

# DO NOT CHANGE
# the player 1 game move
def play1(column):
    global board, cur_player
    if (board[column][-1] == PLAYER1 or board[column][-1] == PLAYER2):
         print ('can\'t place the piece! \n try again')
    else:
        for y in board[column]:
            if (y != PLAYER1 and y != PLAYER2):
                draw_piece(column, 5-y, PLAYER1)
                board[column][y] = PLAYER1
                if (check_for_win(column, y)):
                    print ('player 1 won')
                cur_player = 2
                break

# DO NOT CHANGE
# the player 2 game move
def play2(column):
    global board, cur_player
    if (board[column][-1] == PLAYER1 or board[column][-1] == PLAYER2):
         print ('can\'t place the piece! \n try again')
    else:
        for y in board[column]:
            if (y != PLAYER1 and y != PLAYER2):
                draw_piece(column, 5-y, PLAYER2)
                board[column][y] = PLAYER2
                if (check_for_win(column, y)):
                    print ('player 2 won')
                cur_player = 1
                break

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place0():
    global cur_player
    if (cur_player == 1):
        play1(0)
    elif (cur_player == 2):
        play2(0)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place1():
    global cur_player
    if (cur_player == 1):
        play1(1)
    elif (cur_player == 2):
        play2(1)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place2():
    global cur_player
    if (cur_player == 1):
        play1(2)
    elif (cur_player == 2):
        play2(2)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place3():
    global cur_player
    if (cur_player == 1):
        play1(3)
    elif (cur_player == 2):
        play2(3)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place4():
    global cur_player
    if (cur_player == 1):
        play1(4)
    elif (cur_player == 2):
        play2(4)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place5():
    global cur_player
    if (cur_player == 1):
        play1(5)
    elif (cur_player == 2):
        play2(5)

# functions for placing pieces in each column
# DO NOT CHANGE THESE
def place6():
    global cur_player
    if (cur_player == 1):
        play1(6)
    elif (cur_player == 2):
        play2(6)

# key listeners for placing the pieces
# DO NOT CHANGE THIS
turtle.onkey(place0, '1')
turtle.onkey(place1, '2')
turtle.onkey(place2, '3')
turtle.onkey(place3, '4')
turtle.onkey(place4, '5')
turtle.onkey(place5, '6')
turtle.onkey(place6, '7')

        
# INSERT A LINE HERE TO ACTUALLY DRAW THE BOARD        


turtle.listen()
turtle.mainloop()

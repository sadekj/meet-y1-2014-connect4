import turtle

#pen up and hideing a turtle.
turtle.penup()
turtle.ht()

#initial set of variables
turtle.tracer(0, 0)
CELL_SIZE = 50
BOARD_HIEGHT = 6
BOARD_WIDTH = 7
START_X = -175
START_Y = 125
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


def vert_line(length):
    '''
    Draws a vertical line on the turtle canvas.
    '''
    turtle.pd()
    turtle.sety(turtle.ycor() +length)
 
def horz_line(length):
    '''
    Draws a horizontal line on the turtle canvas.
    '''
    turtle.pd()
    turtle.setx(turtle.xcor() +length)

def draw_board_1(x, y):
    #drawing the board by drawing each cell in a loop
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HIEGHT):
            draw_cell(x,y)
            y -= CELL_SIZE
        y += CELL_SIZE*BOARD_HIEGHT
        x += CELL_SIZE
    turtle.update()

def draw_board(x,y):
    #drawing the board by drawing the lines
    turtle.pendown()
    for i in range(BOARD_WIDTH + 1):
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        vert_line(-BOARD_HIEGHT * CELL_SIZE)
        x += CELL_SIZE
    x -= CELL_SIZE * (BOARD_WIDTH+1)
    
    for i in range(BOARD_HIEGHT + 1):
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()
        horz_line(BOARD_WIDTH * CELL_SIZE)
        y -= CELL_SIZE
    turtle.penup()
    
        

def draw_cell(x, y):
    #drawing a cell in the board
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    horz_line(CELL_SIZE)
    vert_line(-CELL_SIZE)
    horz_line(-CELL_SIZE)
    vert_line(CELL_SIZE)

def draw_piece(column, row, color):
    #
    x = START_X + column * CELL_SIZE
    y = START_Y - row * CELL_SIZE
    turtle.fillcolor(color)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.setpos(x + (CELL_SIZE/2),y - (CELL_SIZE - CELL_SIZE/10 ))
    turtle.begin_fill()
    turtle.pendown()
    turtle.pencolor(color)
    turtle.circle((CELL_SIZE/2) - CELL_SIZE/10)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor("black")

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

def check_for_win(column, row):
    global board
    color = board [column][row]
    if (check_down(column, row, color)):
        return True
    elif (check_row(column, row, color)):
        return True
    elif (check_main_diagonal(column, row, color)):
        return True
    elif (check_sub_diagonal(column, row, color)):
        return True

#checking for wins in each direction
def check_down(column, row, color):
    count = 1
    for i in range(1,4):
        if (row - i >= 0):       
            if(board[column][row - i] == color):
                count +=1
            else:
                count = 0
    if(count == 4):
        return True
    return False

def check_row(column, row, color):
    count = 0
    for i in range(BOARD_WIDTH):
        if(board[i][row] != color):
            count = 0
        elif (board[i][row] == color):
            count += 1
            if(count == 4):
                return True
    return False

def check_main_diagonal(column, row, color):
    count = 1
    for i in range(1,4):
        if (column - i >= 0 and column - i < BOARD_WIDTH and row - i >= 0 and row - i < BOARD_HIEGHT):
            if(board[column - i][row - i] != color):
                break
            elif(board[column - i][row - i] == color):
                count += 1
    for i in range(1,4):
        if (column + i >= 0 and column + i < BOARD_WIDTH and row + i >= 0 and row + i < BOARD_HIEGHT):
            if(board[column + i][row + i] != color):
                break
            elif(board[column + i][row + i] == color):
               count += 1
    if(count == 4):
        return True
    return False

def check_sub_diagonal(column, row, color):
    count = 1
    for i in range(1,4):
        if (column - i >= 0 and column - i < BOARD_WIDTH and row + i >= 0 and row + i < BOARD_HIEGHT):
            if(board[column - i][row + i] != color):
                break
            elif(board[column - i][row + i] == color):
                count += 1  
    for i in range(1,4):
        if (column + i >= 0 and column + i < BOARD_WIDTH and row - i >= 0 and row - i < BOARD_HIEGHT):
            if(board[column + i][row - i] != color):
                break
            elif(board[column + i][row - i] == color):
                count += 1
    if(count == 4):
        return True
    return False

#functions for the key listeners 
def place0():
    global cur_player
    if (cur_player == 1):
        play1(0)
    elif (cur_player == 2):
        play2(0)

def place1():
    global cur_player
    if (cur_player == 1):
        play1(1)
    elif (cur_player == 2):
        play2(1)

def place2():
    global cur_player
    if (cur_player == 1):
        play1(2)
    elif (cur_player == 2):
        play2(2)

def place3():
    global cur_player
    if (cur_player == 1):
        play1(3)
    elif (cur_player == 2):
        play2(3)

def place4():
    global cur_player
    if (cur_player == 1):
        play1(4)
    elif (cur_player == 2):
        play2(4)

def place5():
    global cur_player
    if (cur_player == 1):
        play1(5)
    elif (cur_player == 2):
        play2(5)

def place6():
    global cur_player
    if (cur_player == 1):
        play1(6)
    elif (cur_player == 2):
        play2(6)

#key listeners
turtle.onkey(place0, '1')
turtle.onkey(place1, '2')
turtle.onkey(place2, '3')
turtle.onkey(place3, '4')
turtle.onkey(place4, '5')
turtle.onkey(place5, '6')
turtle.onkey(place6, '7')

        
#drawing the board        
draw_board(START_X , START_Y)

turtle.listen()
turtle.mainloop()

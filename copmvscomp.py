# from tkinter import *
# import random
# from enum import Enum

# class Player(Enum):
#     X = "X"
#     O = "O"

# def next_turn(row, column):
#     global player
#     # Check if the button is empty and the game is not over
#     if buttons[row][column]['text'] == "" and not check_winner():

#         # Set the player's symbol on the button
#         buttons[row][column]['text'] = player.value

#         # Check if the game is won or tied after the move
#         if check_winner():
#             label.config(text=(player.value + " takes the win"))
#         elif not empty_spaces():
#             label.config(text="Issa draw")
#         else:
#             # Switch to the next player's turn
#             player = Player.O if player == Player.X else Player.X
#             label.config(text=(player.value + "s turn"))

#             if player == Player.O:  # Computer's turn
#                 computer_move()

# def check_winner():
#     # Check rows for a win
#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             highlight_winner(row, 0, row, 1, row, 2)
#             return True

#     # Check columns for a win
#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             highlight_winner(0, column, 1, column, 2, column)
#             return True

#     # Check diagonals for a win
#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         highlight_winner(0, 0, 1, 1, 2, 2)
#         return True
#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         highlight_winner(0, 2, 1, 1, 2, 0)
#         return True

#     return False

# def highlight_winner(r1, c1, r2, c2, r3, c3):
#     # Highlight the winning combination of buttons
#     buttons[r1][c1].config(bg=WIN_COLOR)
#     buttons[r2][c2].config(bg=WIN_COLOR)
#     buttons[r3][c3].config(bg=WIN_COLOR)

# def empty_spaces():
#     # Check if there are any empty spaces left on the board
#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] == "":
#                 return True
#     return False

# def new_game():
#     # Start a new game
#     global player
#     player = random.choice(list(Player))
#     label.config(text=player.value + "s turn")

#     # Reset all buttons to empty state
#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="", bg=BUTTON_COLOR)

# # Constants
# BUTTON_COLOR = "black"  # Background color for buttons
# WIN_COLOR = "green"     #color to show winner

# def computer_vs_computer():
#     global player
#     player = random.choice(list(Player))

#     # Start the game loop
#     while empty_spaces() and not check_winner():
#         if player == Player.X:
#             player = Player.O
#         else:
#             player = Player.X
#         computer_move()

#     # Display the result
#     if check_winner():
#         label.config(text=(player.value + " takes the win"))
#     else:
#         label.config(text="Issa draw")

# def evaluate(board):
#     #check for Rows for X or O victory
#     for row in range(3):
#         if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
#             if board[row][0]['text'] == Player.X.value:
#                 return -10
#             elif board[row][0]['text'] == Player.O.value:
#                 return 10

#     # Checking for Columns for X or O victory.
#     for col in range(3):
#         if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
#             if board[0][col]['text'] == Player.X.value:
#                 return -10
#             elif board[0][col]['text'] == Player.O.value:
#                 return 10

#     # Checking for Diagonals for X or O victory.
#     if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
#         if board[0][0]['text'] == Player.X.value:
#             return -10
#         elif board[0][0]['text'] == Player.O.value:
#             return 10

#     if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
#         if board[0][2]['text'] == Player.X.value:
#             return -10  
#         elif board[0][2]['text'] == Player.O.value:
#             return 10

#     # If none of the players has won, return 0
#     return 0

# def minimax(board, depth, isMax):
#     score = evaluate(board)

#     # If the maximizing player has won the game
#     if score == 10:
#         return score

#     # If the minimizing player has won the game
#     if score == -10:
#         return score

#     # If there are no more moves and the game is a tie
#     if not empty_spaces():
#         return 0

#     if isMax:
#         best = -float('inf')
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j]['text'] == "":
#                     board[i][j]['text'] = Player.O.value
#                     best = max(best, minimax(board, depth + 1, not isMax))
#                     board[i][j]['text'] = ""
#         return best

#     else:
#         best = float('inf')
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j]['text'] == "":
#                     board[i][j]['text'] = Player.X.value
#                     best = min(best, minimax(board, depth + 1, not isMax))
#                     board[i][j]['text'] = ""
#         return best  # This function is not needed for computer vs computer game

# def computer_move():
#     best_move = find_best_move(buttons)
#     buttons[best_move[0]][best_move[1]]['text'] = player.value

# def find_best_move(board):
#     # Find the best move for the computer using a simple algorithm
#     for i in range(3):
#         for j in range(3):
#             if board[i][j]['text'] == "":
#                 return i, j  # Return the first empty cell found

# window = Tk()
# window.title("Tic-Tac-Toe")
# window.configure(bg="black") 

# buttons = [[0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0]]

# label = Label(text="Computer vs Computer", font=('white', 40), bg="black", fg="white") 
# label.pack(side="top")

# start_button = Button(text="Start", font=('white', 20), command=computer_vs_computer, bg="black", fg="white") 
# start_button.pack(side="left", anchor="nw")
# reset_button = Button(text="Restart", font=('white', 20), command=new_game, bg="black", fg="white")  # Set button text and background color
# reset_button.pack(side="left", anchor="nw")

# frame = Frame(window, bg="black") 
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="", font=('white', 40), width=5, height=2, bg="black", fg="white") 
#         buttons[row][column].grid(row=row, column=column)

# window.mainloop()
from tkinter import *
import random
from enum import Enum

class Player(Enum):
    X = "X"
    O = "O"

def next_turn(row, column):
    global player
    # Check if the button is empty and the game is not over
    if buttons[row][column]['text'] == "" and not check_winner():

        # Set the player's symbol on the button
        buttons[row][column]['text'] = player.value

        # Check if the game is won or tied after the move
        if check_winner():
            label.config(text=(player.value + " takes the win"))
        elif not empty_spaces():
            label.config(text="Issa draw")
        else:
            # Switch to the next player's turn
            player = Player.O if player == Player.X else Player.X
            label.config(text=(player.value + "s turn"))

            if player == Player.O:  # Computer's turn
                computer_move()

def check_winner():
    # Check rows for a win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            return True

    # Check columns for a win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            highlight_winner(0, column, 1, column, 2, column)
            return True

    # Check diagonals for a win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        return True

    return False

def highlight_winner(r1, c1, r2, c2, r3, c3):
    # Highlight the winning combination of buttons
    buttons[r1][c1].config(bg=WIN_COLOR)
    buttons[r2][c2].config(bg=WIN_COLOR)
    buttons[r3][c3].config(bg=WIN_COLOR)

def empty_spaces():
    # Check if there are any empty spaces left on the board
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def reset_game():
    # Reset the game board and label text
    global player
    player = random.choice(list(Player))
    label.config(text=player.value + "s turn")

    # Reset all buttons to empty state
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=BUTTON_COLOR)

    # Reset button colors
    label.config(bg="black")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg=BUTTON_COLOR)

# Constants
BUTTON_COLOR = "black"  # Background color for buttons
WIN_COLOR = "green"     #color to show winner

def computer_vs_computer():
    global player
    player = random.choice(list(Player))

    # Start the game loop
    while empty_spaces() and not check_winner():
        if player == Player.X:
            player = Player.O
        else:
            player = Player.X
        computer_move()

    # Display the result
    if check_winner():
        label.config(text=(player.value + " takes the win"))
    else:
        label.config(text="Issa draw")

def evaluate(board):
    #check for Rows for X or O victory
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            if board[row][0]['text'] == Player.X.value:
                return -10
            elif board[row][0]['text'] == Player.O.value:
                return 10

    # Checking for Columns for X or O victory.
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            if board[0][col]['text'] == Player.X.value:
                return -10
            elif board[0][col]['text'] == Player.O.value:
                return 10

    # Checking for Diagonals for X or O victory.
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        if board[0][0]['text'] == Player.X.value:
            return -10
        elif board[0][0]['text'] == Player.O.value:
            return 10

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        if board[0][2]['text'] == Player.X.value:
            return -10  
        elif board[0][2]['text'] == Player.O.value:
            return 10

    # If none of the players has won, return 0
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)

    # If the maximizing player has won the game
    if score == 10:
        return score

    # If the minimizing player has won the game
    if score == -10:
        return score

    # If there are no more moves and the game is a tie
    if not empty_spaces():
        return 0

    if isMax:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]['text'] == "":
                    board[i][j]['text'] = Player.O.value
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j]['text'] = ""
        return best

    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]['text'] == "":
                    board[i][j]['text'] = Player.X.value
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j]['text'] = ""
        return best  # This function is not needed for computer vs computer game

def computer_move():
    best_move = find_best_move(buttons)
    buttons[best_move[0]][best_move[1]]['text'] = player.value

def find_best_move(board):
    # Find the best move for the computer using a simple algorithm
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == "":
                return i, j  # Return the first empty cell found

window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="black") 

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text="Computer vs Computer", font=('white', 40), bg="black", fg="white") 
label.pack(side="top")

start_button = Button(text="Start", font=('white', 20), command=computer_vs_computer, bg="black", fg="white") 
start_button.pack(side="left", anchor="nw")

reset_button = Button(text="Reset", font=('white', 20), command=reset_game, bg="black", fg="white") 
reset_button.pack(side="left", anchor="nw")

frame = Frame(window, bg="black") 
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('white', 40), width=5, height=2, bg="black", fg="white") 
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

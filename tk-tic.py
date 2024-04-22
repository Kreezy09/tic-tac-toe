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

def new_game():
    # Start a new game
    global player
    player = random.choice(list(Player))
    label.config(text=player.value + " turn")

    # Reset all buttons to empty state
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=BUTTON_COLOR)

# Constants
BUTTON_COLOR = "black"  # Background color for buttons
WIN_COLOR = "green"     # Color to highlight winning buttons

window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="black")  # Set window background color to black

player = random.choice(list(Player))

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player.value + "s turn", font=('white', 40), bg="black", fg="white")  # Set label text color to white
label.pack(side="top")

reset_button = Button(text="Restart", font=('white', 20), command=new_game, bg="black", fg="white")  # Set button text and background color
reset_button.pack(side="left", anchor="nw")

frame = Frame(window, bg="black")  # Set frame background color to black
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('white', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column), bg=BUTTON_COLOR, fg="white")  # Set button text color to white
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

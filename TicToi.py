import tkinter as tk
from tkinter import messagebox

# Define constants for the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Define the initial state of the game
initial_state = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]

# Initialize the player (X goes first)
current_player = PLAYER_X

# Function to check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for cell in board)

# Function to check if a player has won
def check_win(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to evaluate the game state
def evaluate(board):
    if check_win(board, PLAYER_X):
        return -1
    elif check_win(board, PLAYER_O):
        return 1
    elif is_board_full(board):
        return 0
    return None

# Minimax algorithm for AI move
def minimax(board, depth, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
        return min_eval

# AI's move
def ai_move():
    if is_board_full(board):
        return

    best_move = None
    best_eval = -float("inf")

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            eval = minimax(board, 0, False)
            board[i] = EMPTY

            if eval > best_eval:
                best_eval = eval
                best_move = i

    if best_move is not None:
        buttons[best_move].config(text=PLAYER_O, state=tk.DISABLED)
        board[best_move] = PLAYER_O
        check_game_over()

# Function to handle player's move
def player_move(idx):
    if board[idx] == EMPTY:
        buttons[idx].config(text=PLAYER_X, state=tk.DISABLED)
        board[idx] = PLAYER_X
        check_game_over()
        ai_move()

# Function to check if the game is over
def check_game_over():
    if check_win(board, PLAYER_X):
        messagebox.showinfo("Tic-Tac-Toe", "You win!")
        reset_game()
    elif check_win(board, PLAYER_O):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        reset_game()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_game()

# Function to reset the game
def reset_game():
    global board, current_player
    board = initial_state
    current_player = PLAYER_X

    for button in buttons:
        button.config(text=EMPTY, state=tk.NORMAL)

# Create the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []

for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=EMPTY, width=10, height=3,
                       command=lambda idx=i: player_move(idx))
    button.grid(row=row, column=col)
    buttons.append(button)

board = initial_state

root.mainloop()

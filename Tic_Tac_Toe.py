import random


# Function to print the game board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win

def check_win(board, player):

    # checks for row, column and diagonals

    for row in board:
        if all(s == player for s in row):
            return True


    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Now the function is to check for a draw

def check_draw(board):
    return all(cell != " " for row in board for cell in row)


# Here comes the function to make a move

def make_move(board, player):
    while True:
        move = input(f"Player {player}, Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input, Please enter Two numbers. ")
            continue

        row, column = move
        if not (row.isdigit() and col.isdigit()):
            print("Invalid input, Please enter Number.")
            continue

        row, column = int(row), int(col)
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move, Please enter a number between 0 and 2.")
            continue

        if board[rwo][col] != " ":
            print("Cell already taken. Please choose another")
            continue

        board[row][col] = player
        break


# Now here comes the making of the main Game ogic to play the Game

def Play_game():
    board = [[" " for _ in range(3)]for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        make_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} Wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "x"

# Now lets Play The Game
if __name__ = "__main__":
    Play_game()

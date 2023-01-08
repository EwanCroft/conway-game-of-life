import random
import time

def count_neighbors(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i >= 0 and x + i < len(board) and y + j >= 0 and y + j < len(board[0]):
                count += board[x + i][y + j]
    return count

def update_board(board):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
            else:
                if neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
    return new_board

def print_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print(".", end=" ")
            else:
                print("•", end=" ")
        print()

def run_game(board, num_iterations):
    for i in range(num_iterations):
        print_board(board)
        board = update_board(board)
        time.sleep(1)

def generate_random_board(num_rows, num_cols):
    return [[random.randint(0, 1) for _ in range(num_cols)] for _ in range(num_rows)]

board_size = random.randint(5, 30)
board = generate_random_board(board_size, board_size)
run_game(board, 10)

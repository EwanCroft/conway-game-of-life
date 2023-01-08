import random
import tkinter as tk

class GameOfLifeGUI:
    def __init__(self, num_rows, num_cols, num_iterations):
        self.board = generate_random_board(num_rows, num_cols)
        self.num_iterations = num_iterations
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=num_cols*10, height=num_rows*10)
        self.canvas.pack()
        self.draw_board()
        self.root.after(1000, self.run_game)
        self.root.mainloop()

    def draw_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    color = "black"
                else:
                    color = "white"
                self.canvas.create_rectangle(j*10, i*10, (j+1)*10, (i+1)*10, fill=color)

    def run_game(self):
        self.board = update_board(self.board)
        self.draw_board()
        self.num_iterations -= 1
        if self.num_iterations > 0:
            self.root.after(250, self.run_game)

def count_neighbours(board, x, y):
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
            neighbours = count_neighbours(board, i, j)
            if board[i][j] == 1:
                if neighbours == 2 or neighbours == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
            else:
                if neighbours == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
    return new_board

def generate_random_board(num_rows, num_cols):
    return [[random.randint(0, 1) for _ in range(num_cols)] for _ in range(num_rows)]

board_size = 30
game_length = random.randint(10, 25)
GameOfLifeGUI(board_size, board_size, game_length)
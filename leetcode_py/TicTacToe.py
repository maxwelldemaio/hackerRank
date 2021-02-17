""" Create a game of Tic Tac Toe
0's represent emptiness, 1's represent Xs,
2's represent Os
"""
import os
os.system("cls") # clear for linux

class Board():
    # Initialize board object (empty)
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def display(self):
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("---------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("---------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")

# Make board instance
board = Board()
# display the board
board.display()

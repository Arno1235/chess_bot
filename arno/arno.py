import chess

import random


class Bot():
    def __init__(self):
        pass

    def getName(self):
        return "Arno"

    def move(self, board):
        moves = list(board.legal_moves)

        return random.choice(moves)

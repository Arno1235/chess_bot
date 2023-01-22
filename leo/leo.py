import chess


class Bot():
    def __init__(self):
        pass

    def getName(self):
        return "Leo"

    def move(self, board):
        move = chess.Move.from_uci("e2e4")
        return move

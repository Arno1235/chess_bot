import chess


class Bot():
    def __init__(self):
        pass

    def getName(self):
        return "Arno"

    def move(self, board):
        move = chess.Move.from_uci("e7e6")
        return move

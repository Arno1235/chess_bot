import chess
from stockfish import Stockfish


class Bot():
    def __init__(self):
        self.stockfish = Stockfish(depth=9, parameters={
                                   "Threads": 1, "Minimum Thinking Time": 1})

    def getName(self):
        return "Stockfish"

    def move(self, board):
        self.stockfish.set_fen_position(board.fen())
        move = chess.Move.from_uci(self.stockfish.get_best_move())
        return move

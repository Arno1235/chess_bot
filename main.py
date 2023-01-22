# TEMPLATE

import random
import time

import chess

import leo.leo as leo
import arno.arno as arno

TIME_PER_MOVE = 3

if __name__ == "__main__":

    board = chess.Board()

    Leo_bot = leo.Bot()
    Arno_bot = arno.Bot()

    chess_bots = [Leo_bot, Arno_bot]
    random.shuffle(chess_bots)

    print(
        f'{chess_bots[0].getName()} is white and {chess_bots[1].getName()} is black')

    while not board.outcome():

        if board.turn == chess.WHITE:

            start = time.time()
            move = chess_bots[0].move(board)
            if time.time() - start > TIME_PER_MOVE:
                print(
                    f'{chess_bots[0].getName()} (white) took too long to move')
                break

            if move in board.legal_moves:
                board.push(move)
            else:
                print(
                    f'{chess_bots[0].getName()} (white) made an illegal move')
                break
        else:

            start = time.time()
            move = chess_bots[1].move(board)
            if time.time() - start > TIME_PER_MOVE:
                print(
                    f'{chess_bots[1].getName()} (black) took too long to move')
                break

            if move in board.legal_moves:
                board.push(move)
            else:
                print(
                    f'{chess_bots[1].getName()} (black) made an illegal move')
                break

        print(board)

    if board.is_checkmate():
        if board.turn == chess.WHITE:
            print(f'{chess_bots[1].getName()} (black) has won!')
        else:
            print(f'{chess_bots[0].getName()} (white) has won!')
    else:
        print(board.outcome())

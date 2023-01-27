# TEMPLATE
import pretty_errors

import random
import time

import chess

import leo.leo as leo
import arno.arno as arno
import custom_stockfish.custom_stockfish as custom_stockfish

TIME_PER_MOVE = 3

if __name__ == "__main__":

    board = chess.Board()

    Leo_bot = leo.Bot()
    Arno_bot = arno.Bot()
    Stockfish_bot = custom_stockfish.Bot()

    chess_bots = [Stockfish_bot, Leo_bot]
    # chess_bots = [Leo_bot, Arno_bot]

    random.shuffle(chess_bots)

    print(
        f'{chess_bots[0].getName()} is white and {chess_bots[1].getName()} is black')

    move_counter = 0

    while not board.outcome():

        move_counter += 1

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
        print(f'move {move_counter}')

    if board.is_checkmate():
        if board.turn == chess.WHITE:
            print(
                f'{chess_bots[1].getName()} (black) has won in {move_counter} moves!')
        else:
            print(
                f'{chess_bots[0].getName()} (white) has won in {move_counter} moves!')
    else:
        print(board.outcome())

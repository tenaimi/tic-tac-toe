from src.board import Board
from random import randint


class Player:
    def __init__(self, name, character, is_human):
        self.name = name
        self.character = character
        self.is_human = is_human

    def play_turn(self):
        if self.is_human == True:
            print()

    def play(self, list_2D):
        if list_2D == None:
            list_2D = Board().draw_board()
        else:
            Board().draw_board()
        if not self.is_human:
            return self.computer(list_2D)
        return self.human(list_2D)

    def human(self, list_2D):
        pass

    def read_position(self, list_2D, position):  # human play handler
        coord = input(
            "Play by choosing and (x, y) co-ordinate on the board i.e; 01, 12, 21: ")
        board = Board()
        #board.draw_board()
        x = int(coord[0])
        y = int(coord[1])

        return list_2D

    def computer(self, list_2D):
        move = self.computer_play(list_2D)
        print(self.name + ' entered number ' + str(move))
        ctx = self.insert_character(move, list_2D)
        return Board().update_board(ctx)

    def computer_play(self, list_2D):  # computer play handler
        # return random position within constriant
        pass

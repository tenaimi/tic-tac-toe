#from game import Game
from src.board import Board

def main():
    booard = Board()
    booard.draw_board()
    booard.update_board([["x", " ", "o"], ["o", " ", "o"], ["x", " ", "o"]])
main()
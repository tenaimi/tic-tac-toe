from src.board import Board
from src.player import Player

class Game:
    def __init__(self):
        self.initialize_game()
        self.play()
        self.available_characters = ['X', 'O']
    
    def initialize_game(self):
        print('---------------')
        print(' Tic Tac Toe   ')
        print('---------------\n')
    
    def play(self):
       name = input("Enter your name: ")
       character = input("Enter your character (X or O): ").upper()
       while character != 'X' and character != 'O':
           character = input("Please re-enter your character (X or O): ")
       is_human = True
       board = Board()
       self.available_characters.remove(character)

       player = Player(name, character, is_human)
       computer = Player("Computer", self.available_characters[0], not is_human)

       print("Play by choosing and (x, y) co-ordinate on the board")
       board.draw_board()

    


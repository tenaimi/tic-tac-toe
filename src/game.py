from src.board import Board
from src.player import Player

class Game:
    def __init__(self):
        self.initialize_game()
    
    def initialize_game(self):
        print('---------------')
        print(' Tic Tac Toe   ')
        print('---------------\n')
    
    def start(self):
       available_characters = ['X', 'O']
       name = input("Enter your name: ")
       character = input("Enter your character (X or O): ").upper()
       while character.upper() != 'X' and character.upper() != 'O':
           character = input("Please re-enter your character (X or O): ")
       is_human = True
       board = Board()
       available_characters.remove(character)

       player = Player(name, character, is_human)
       computer = Player("Computer", available_characters[0], not is_human)
       board.draw_board
       n = 0

       while not self.game_over() and n <= 9:
           if n%2 == 1:
               computer.play(board)
               n += 1
           else:
                player.play(board)
                n += 1
    
    def game_over(self):
        return False
        #test result in 2d_arr


    


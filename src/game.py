from src.player import Player

class Game:
    def __init__(self):
        self.initialize_game()
    
    def initialize_game(self):
        print('-------------------------')
        print(' Welcome To Tic Tac Toe  ')
        print('-------------------------')
    
    def start(self):
       available_characters = ['X', 'O']
       name = input("Enter your name: ")
       character = input("Enter your character (X or O): ").upper()
       while character != 'X' and character != 'O':
           character = input("Please re-enter your character (X or O): ")
       is_human = True
       available_characters.remove(character)

       human = Player(name, character, is_human)
       computer = Player("Computer", available_characters[0], not is_human)
       
       context = None
       control = self.game_over(context)
       
       while not control:
        context = human.play(context)
        control = self.game_over(context)
        context = computer.play(context)
        control = self.game_over(context)
    
    def game_over(self, nested_array):
        return False
from random import randint
from src.board import Board

class Player:
    def __init__(self, name, character, is_human):
        self.name = name
        self.character = character
        self.is_human = is_human
        self.proceed = True
    
    def play(self, nested_array):
        if nested_array == None:
            nested_array = Board().draw_board()
        else:
            Board().draw_board()
        if not self.is_human:
            return self.computer(nested_array)
        return self.human(nested_array)
       

    def computer(self, nested_array):
        move = self.computer_play(nested_array)
        print(self.name + ' entered number ' + str(move))
        ctx = self.insert_character(move, nested_array)
        return Board().update_board(ctx)
    
    def human(self, nested_array):
        position = input(self.name + " play by entering a number (1 - 9): ")
        ctx = self.insert_character(position, nested_array)
        return Board().update_board(ctx)
      
    def insert_character(self, position, nested_array):
        counter = 0
        for i in range(len(nested_array)):
            for j in range(len(nested_array[i])):
                counter += 1
                if int(counter) == int(position):
                    if nested_array[i][j] == 'X' or nested_array[i][j] == 'O':
                        print(str(counter) + " is not available. Try Again " + self.name)
                        self.proceed = False
                        return nested_array
                    nested_array[i][j] = self.character
                if nested_array[i][j] != 'X' and nested_array[i][j] != 'O':
                    nested_array[i][j] = ' '
        return nested_array
    
    def computer_play(self, nested_array):
        counter = 0
        possible_choices = []
        for i in range(len(nested_array)):
            for j in range(len(nested_array[i])):
                counter += 1
                if nested_array[i][j] == ' ':
                    possible_choices.append(counter)
        random_choice = randint(0, len(possible_choices) - 1)
        return possible_choices[int(random_choice)]

                   
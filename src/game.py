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
            if computer.proceed:
                context = human.play(context)
                control = self.game_over(context)
            if human.proceed:
                context = computer.play(context)
                control = self.game_over(context)

    def game_over(self, nested_array):
        if nested_array != None:
            for i in range(len(nested_array)):
                for j in range(len(nested_array[i])):
                    #print(i, j)
                    content = nested_array[i][j]
                    # print(content)
                    if i == 0 and content != " ":
                        # check vertical
                        if content == nested_array[i+1][j] and content == nested_array[i+2][j]:
                            print(content, " is the Winner!!")
                            return True
                    if j == 0 and content != " ":
                        # check horizontal
                        if content == nested_array[i][j+1] and content == nested_array[i][j+2]:
                            print(content, " is the Winner!!")
                            return True
                    if (i == 0 and j == 0) and content != " ":
                        # check forward diagonal
                        if content == nested_array[i+1][j+1] and content == nested_array[i+2][j+2]:
                            print(content, " is the Winner!!")
                            return True
                    if (i == 0 and j == 2) and content != " ":
                        # check backward diagonal
                        if content == nested_array[i+1][j-1] and content == nested_array[i+2][j-2]:
                            print(content, " is the Winner!!")
                            return True
        return False

class Player:
    def __init__(self, name, character, is_human):
        self.name = name
        self.character = character
        self.is_human = is_human
    
    def play_turn(self, x, y):
        if self.is_human == True:
            self.human()
        #print() character in location x, y on board
      

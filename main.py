#from src.game import Game
import re

def main():
    #game = Game()
    #game.start()
    reg = r'([0-2|\d][0-5?|\d][0-5?]\.?){4}'
    ip1 = "192.168.0.255"
    matched = re.match(reg, ip1)
    if matched:
        print(matched)
    else:
        print("no match")
    
main()
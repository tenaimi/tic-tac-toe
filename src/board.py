class Board:
    def __init__(self):
        self.size = 3
        self.board = self.twoD_arr()

    def draw_board(self):
        for i in range(self.size):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end='')
                if j != 2:
                    print(" | ", end='')
            print("")

    def twoD_arr(self):
        result = []
        for _ in range(self.size):
            item = []
            for _ in range(self.size):
                item.append(" ")
            result.append(item)
        return result

    def update_board(self, board):
        for i in range(self.size):
            for j in range(len(board[i])):
                print(board[i][j], end='')
                if j != 2:
                    print(" | ", end='')
            print("")

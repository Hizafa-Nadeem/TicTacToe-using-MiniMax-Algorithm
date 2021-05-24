


class Tictactoe:

    def __init__(self):
        self.isMax = True
        self.move = 0
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

    def display_board(self):
        line =""
        print("----------------")
        for i in range(1, 10):
            line += "| "+ self.board[i]+" |"

            if i % 3 == 0:
                print(line, "\n----------------")
                line = ""


    def start_game(self):
        print("New Game!")
        self.display_board()

        mark = input("Which player will make a move: X for AI, O for Human")
        if mark == 'X':
             self.isMax = True
             self.move = 1
             self.board[1] = 'X'
        else:
            self.isMax = False
            self.move = int(input("Oye Human! your turn:"))
            #print(self.b_ind[(self.move)])
            self.board[self.move] = 'O'

        self.display_board()

        self.minimax(self.board)

    def check_Win(self):
        i = 1
        while( i <= 3 ):
            if self.board[i] == self.board[i+1] == self.board[i+2] == 'X':
                return 'X'
            i += 3
        i = 1
        while (i <= 3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == 'X':
                return 'X'
            i += 1
        if self.board[1] == self.board[5] == self.board[9] == 'X':
            return 'X'
        if self.board[1] == self.board[5] == self.board[9] == 'X':
            return 'X'
        # check for Human Win

        while (i <= 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return True
            i += 3
        i = 1
        while (i <= 3):            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True
            i += 1
        if self.board[1] == self.board[5] == self.board[9] :
            return True
        if self.board[1] == self.board[5] == self.board[9] :
            return True
        else:
            for ind in range(1,10):
                if self.board[i] == 'X' or self.board[i] == 'O' or

            return True







    def minimax(self, board):
        if self.check_Win() == True:
            pass















# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Game = Tictactoe()
    Game.start_game()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

map = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
class Tictactoe:

    def __init__(self):
        self.board = [[' ', ' ', ' '] for i in range(3)]


    def isMovesLeft(self):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == ' '):
                    return True
        return False

    def isTerminal(self,b):

        # Checking for Rows for X or O victory.
        for row in range(3):
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == 'X'):
                    return 1
                elif (b[row][0] == 'O'):
                    return -1

        # Checking for Columns for X or O victory.
        for col in range(3):

            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

                if (b[0][col] == 'X'):
                    return 1
                elif (b[0][col] == 'O'):
                    return -1

        # Checking for Diagonals for X or O victory.
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

            if (b[0][0] == 'X'):
                return 1
            elif (b[0][0] == 'O'):
                return -1

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

            if (b[0][2] == 'X'):
                return 1
            elif (b[0][2] == 'O'):
                return -1

        # Else if none of them have won then return 0
        return 0

    def select_best_move(self):
        best_move = [-1,-1]
        score =self.minimax(self.board,False,best_move)
        return best_move
    def minimax(self,board,isMax,best_move):
        score = self.isTerminal(board)
        return score,

        if isMax == True:
            Max_score = 2

            for i in range(3):
                for j in range(3):
                    if board[i][j]== ' ':
                        board[i][j]= 'X'
                        child_score=minimax(board,False)
                        board[i][j] = ' '
                        Max_score= max(child_score,Max_score)
                        if child_score> Max_score:
                            best_move = [i,j]
            return Max_score

        elif isMax == False:
            Min_score = -2

            for i in range(3):
                for j in range(3):
                    if board[i][j]== ' ':
                        board[i][j]= 'O'
                        child_score=minimax(board,True)
                        board[i][j] = ' '
                        Min_score= min(child_score,Min_score)
                        if child_score < Min_score:
                            best_move = [i,j]

            return Min_score

    def display_board(self):
        line =""
        print("----------------")
        for i in range(3):
            for j in range(3):
                line += "| " + self.board[i][j] + " |"
            print(line, "\n----------------")
            line = ""

    def play_game(self):

        print("New Game!\n")
        self.display_board()
        turn = input("Which player will make a move: X for AI, O for Human")
        while self.isMovesLeft() == True:

            if turn == 'X':
                print("AI makes move !")
                best_move = self.select_best_move()
                self.board[best_move[0]][best_move[1]] = 'X'
                turn ='O'
            else:
                cell = int(input("Oye Human! make your move:"))
                self.board[map[cell][0]][map[cell][1]] = 'O'
                turn = 'X'


            self.display_board()
        #AnnounceWinner

if __name__ == '__main__':

    Game = Tictactoe()
    Game.play_game()

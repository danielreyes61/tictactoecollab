class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    # Working.
    def __init__(self):
        self.board = [["O",'O',"O"],["O","O",None],["O","O","O"]]
        self.wholeBoard = []
        self.fullBoard = False
        self.player1 = None
        self.player2 = None
        self.win_condition = None
        self.is_full_condition = None

    # index out of range
    def calc_winner(self):
        for space in range(3):
            # Loops through columns to check for vertical win.
            if self.board[space] == 'X' and self.board[space+3] == 'X' and self.board[space+6] == 'X':
                self.win_condition == True

            # Loops though rows to check for horizontal win
            elif self.board[(space*3)] == 'X' and self.board[(space*3)+1] == 'X' and self.board[(space*3)+2] == 'X':
                self.win_condition == True

            # Loops through and checks for either possible diagonal win
            elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
                self.win_condition == True

            elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
                self.win_condition == True
            # Handle no winner condition and 'O' winner condition


    # Working.
    def is_full(self):
        self.wholeBoard = self.board[0] + self.board[1] + self.board[2]
        if any(x is None for x in self.wholeBoard):
            self.is_full_condition = False
        else:
            self.is_full_condition = True

    # Working.
    def is_game_over(self):
        if self.is_full_condition == True:
            print("No more spaces")
            #Game.calc_winner(self)

        elif self.win_condition == True:
            print("Winner")

    # Working.   
    def __repr__(self):
        print(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}")
   
    #Working
    def move(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player.token
        if self.board[y][x] == None:
            self.board[y][x] = player.token    
        print(self.x, self.y, player.token)       
    

p1 = Player("Dan", "X")
p2 = Player("Ted", "O")
g1 = Game()
g1.player1 = p1
g1.player2 = p2
#print(p1.name + p1.token)
#g1.is_full()
#print(g1.is_full_condition)
#g1.is_game_over()

g1.__repr__()
g1.move(2,1,p1)
g1.__repr__()

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self):
        self.board = [["X",None,"X"],["O","O","X"],["X","X","X"]]
        self.fullBoard = False
        self.x = -1
        self.y = -1
        self.player1 = None
        self.player2 = None
        self.win_condition = None
        self.is_full_condition = None

    def move(self):
        pass

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

    def is_full(self):
        for spot in self.board:
            if spot != None:
                self.is_full_condition = True
            else:
                self.is_full_condition = False
                #return self.fullBoard == True
            #else:
                #continue

    def is_game_over(self, calc_winner, is_full):
        if self.fullBoard == True:
            outcome = 'No more spaces. GG.'
        elif self.win_condition == True:
            outcome = f''

            
def __repr__(self,board):
    print(f"{board[0]}\n{board[1]}\n{board[2]}")
    pass

p1 = Player("Dan", "X")
p2 = Player("Ted", "O")
g1 = Game()
g1.player1 = p1
g1.player2 = p2

print(p1.name + p1.token)
g1.is_full()
print(g1.is_full_condition)


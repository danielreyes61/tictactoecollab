class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self, board = [[None,None,None],[None,None,None],[None,None,None]] ):
        self.board = board

    def move(x,y, player):
        pass

    def calc_winner():
        pass 

    def calc_winner():
        for space in range(3):
            # Loops through columns to check for vertical win.
            if self.board[space] == 'X' and self.board[space+3] == 'X' and self.board[space+6] == 'X':
                return win_condition == True

            # Loops though rows to check for horizontal win
            elif self.board[(space*3)] == 'X' and self.board[(space*3)+1] == 'X' and self.board[(space*3)+2] == 'X':
                return win_condition == True

            # Loops through and checks for either possible diagonal win
            elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
                return win_condition == True

            elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
                return win_condition == True

    def is_full(self, board):
        for spot in self.board:
            if spot != None:
                return fullBoard == True
            else:
                continue


    def is_game_over(self):
        if fullBoard == True:
            outcome = 'No more spaces. GG.'
        elif win_condition == True:
            outcome = f''

            
def __repr__(self):
    pass

g1 = Game()
g1.is_full(board)

p1 = Player("Dan", "X")
print(p1.name + p1.token)


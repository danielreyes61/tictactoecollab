class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        board = [["X","O","X"],["O","O","X"],["X","X","X"]]
        self.board = board
        self.fullBoard = False
        
        def move(x,y, player):
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
                    return 

        def is_full(self, board):
            for spot in self.board:
                print(spot)

        def is_game_over(self):
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
                    return
                
        def __repr__(self):
            pass

g1 = Game()
g1.is_full()
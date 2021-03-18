class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    # Working
    def __init__(self):
        self.board = [[None,None,None],[None,None,None],[None,None,None]]
        self.wholeBoard = []
        self.fullBoard = False
        self.player1 = None
        self.player2 = None
        self.win_condition = None
        self.is_full_condition = None


    # Maybe Working
    def is_full(self):
        self.wholeBoard = self.board[0] + self.board[1] + self.board[2]
        if any(x is None for x in self.wholeBoard):
            self.is_full_condition = False
        else:
            self.is_full_condition = True

    # Working
    def is_game_over(self):
        if self.is_full_condition == True:
            print("No more spaces")


        elif self.win_condition == True:
            print("Winner")

    # Working
    def __repr__(self):
        print(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}")
   
    # Working
    def move(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player.token
        if self.board[y][x] == None:
            self.board[y][x] = player.token    
        


    # Working
    def calc_winner(self):

            #Horizontal wins (columns)
        if self.board[0][0] != None and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            print('column win ' + self.board[0][0])
            self.win_condition = self.board[0][0]
            self.__repr__()

        elif self.board[0][1] != None and self.board[0][1] == self.board[1][1] == self.board[2][1]:
            print('column win ' + self.board[0][1])
            self.win_condition = self.board[0][1]
            self.__repr__()

        elif self.board[0][2] != None and self.board[0][2] == self.board[1][2] == self.board[2][2]:
            print('column win ' + self.board[0][2])
            self.win_condition = self.board[0][2]
            self.__repr__()

            #Vertical wins (rows)
        elif self.board[0][2] != None and self.board[0][0] == self.board[0][1] == self.board[0][2]:
            print('row win ' + self.board[0][0])
            self.win_condition = self.board[0][0]
            self.__repr__()

        elif self.board[1][2] != None and self.board[1][0] == self.board[1][1] == self.board[1][2]:
            print('row win ' + self.board[1][0])
            self.win_condition = self.board[1][0]
            self.__repr__()

        elif self.board[2][2] != None and self.board[2][0] == self.board[2][1] == self.board[2][2]:
            print('row win ' + self.board[2][0])
            self.win_condition = self.board[2][0]            
            self.__repr__()

            #Diagonal wins
        elif self.board[2][2] != None and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            print('top-left diagonal win ' + self.board[0][0])
            self.win_condition = self.board[0][0]
            self.__repr__()

        elif self.board[0][2] != None and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            print('top-right diagonal win ' + self.board[0][0])
            self.win_condition = self.board[2][0]
            self.__repr__()            

      

p1 = Player("Dan", "X")
p2 = Player("Ted", "O")
g1 = Game()
g1.player1 = p1
g1.player2 = p2
player_input = ""
choose_x_coord = ""
choose_y_coord = ""

while True:
    if g1.is_game_over == True:
        g1.calc_winner()
        g1.__repr__()
        break
    g1.__repr__()
    player_input = input("Choose player, please enter p1 or p2: ")
    if player_input == "p1":
        player_input = p1
    if player_input == "p2":
        player_input = p2
    choose_x_coord = int(input("Please enter a X coordinate: "))
    choose_y_coord = int(input("Please enter a Y coordinate: "))
    g1.move(choose_x_coord,choose_y_coord,player_input)
    g1.is_game_over()
    g1.calc_winner()
    if g1.win_condition != None:
        break






class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token



class Game:

    board = [[None,None,None],[None,None,None],[None,None,None]]

    def move(x,y, player):
        pass


    def calc_winner():
        pass 

    def is_full():
        pass

    def is_game_over():
        pass



    def __repr__(self):
        pass

g1 = Game()
print(g1.board)

p1 = Player("Dan", "X")
print(p1.name + p1.token)



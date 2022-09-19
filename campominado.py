# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new object", or
# "dig here", or "render this game for this object"

class board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters, they'll be helpfull later
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        
        # 





# play the game
def play(dim_size=10, num_bombs=10):
    # step1: create the board and plant the bombs
    # step2: show the user the board and ask for where they want to dig
    # step3a: if location is a bomb, show game over message
    # step3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory
    pass 
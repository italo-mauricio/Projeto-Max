# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new object", or
# "dig here", or "render this game for this object"

class board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters, they'll be helpfull later
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # let's create the board
        # helper function!
        
        self.board = self.make_new_board() # plant the bombs
        
        
        
        # initialize a set to keep track of which locations we've uncovered
        # we'll (row, col) tuples into this set
        self.dug = set() # if we dig at 0, 0, then self.bug = {(0,0)}
    
    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)
        
        # generete a new board
        
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # this create an array like this:
        # [[None, None, ..., None]],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]
        # we can see how this represents a board!
        
                
 




# play the game
def play(dim_size=10, num_bombs=10):
    # step1: create the board and plant the bombs
    # step2: show the user the board and ask for where they want to dig
    # step3a: if location is a bomb, show game over message
    # step3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory
    pass 
import random

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
        self.assign_vlaues_to_board()
        
        
        
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
        
        # plant the bombs
        bomb_planted = 0
        while bomb_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) # return random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell 
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to loo
            
            if board[row][col] == '*':
                # this means we've actually planted a bomb there alredy so keep going
                continue
            
            board[row][col] = '*' # plant the bomb
            bombs_planted += 1
            
        return board 

    def assign_valuews_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. We can precompute these and it'll save us some
        # effort checking what's around the board later on. 
        
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
                
                
    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row=1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+!)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)
        
        # make sure to not go out of bounds!
        
        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
                    
        return num_neighboring_bombs
    
    def dig(self, row, col):
        # dig at that location:
        # return True if sucessful dig, False if bomb dug
        
        # a few scenarios:
        # hit a bom -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!
        
        self.dug.add((row, col))  # keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0,row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
        
        return True            
                
        




# play the game
def play(dim_size=10, num_bombs=10):
    # step1: create the board and plant the bombs
    board = board(dim_size, num_bombs)
    
    
    # step2: show the user the board and ask for where they want to dig
    # step3a: if location is a bomb, show game over message
    # step3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # step4: repeat steps 2 and 3a/b until there are no more places to dig -> Victory
    pass  
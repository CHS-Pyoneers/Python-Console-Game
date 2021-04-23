
# NOTE: ALL LOCATIONS ARE IN y, x
# because i keep forgetting

def kingMoves(board, location):
    '''
    get all legal moves for a king piece

    board: Board array
    location: index of the target piece
    '''

    is_black = board[location[0]][location[1]].isupper()
    available_moves = []
    moves_to_check = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for move in moves_to_check:
        try:
            target = board[location[0] + move[0]][location[1] + move[1]]
            if target == " " or target.isupper() != is_black:
                available_moves.append([location[0]+move[0], location[1]+move[1]])
        except IndexError:
            pass
    return available_moves


# maps every piece to a function that gets it's valid moves
moves_dictionary = {
    "k": kingMoves,
    "q": None,
    "b": None,
    "n": None,
    "r": None,
    "p": None
}

class Board:
    def __init__(self):
        '''
        Pieces:
        k - king
        q - queen
        b - bishop
        n - knight
        r - rook
        p - pawn
        - uppercase letters represent black pieces and lower case represent white pieces
        '''
        self.board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                      ["P", "P", "P", "P", "P", "P", "P", "P"],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      ["p", "p", "p", "p", "p", "p", "p", "p"],
                      ["r", "n", "b", "q", "k", "b", "n", "r"],]

        # turnNum increments every time a move is made
        # if it's odd its whites turn if its even its blacks turn
        self.turnNum = 1
        self.gameIsOver = False


    def printBoard(self):
        # Displays the board to the user
        print(self.board)
        # Need a better way to display board to user


    def getInput(self):
        # Gets a move from the user and then returns the index of
        # the target piece and the index of the target location
        print("Input Move:")
        raw_move = input()
        # process the raw input here


    def makeMove(self, piece_location, target_location, special=None):
        # Moves a piece on the board from one position to the other
        # Should only be called after the move is confirmed to be valid
        if special is None:
            self.board[target_location[0]][target_location[1]] = self.board[piece_location[0]][piece_location[1]]
            self.board[piece_location[0]][piece_location[1]] = ' '
        elif special == "castle":
            # add code to handle castling here
            pass
        elif special == "en passant":
            # add code for en passant here
            pass

if __name__ == "__main__":
    board = Board()
    board.printBoard()

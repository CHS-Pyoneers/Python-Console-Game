


def kingMoves(board, isBlack, index):
    '''
    get all legal moves for a king piece

    board: Board object
    isBlack: boolean whether the target piece is black
    index: index of the target piece
    '''
    available_moves = []
    moves_to_check = [-11, -10, -9, -1, 1, 9, 10, 11]
    for move in moves_to_check:
        target = board.board[index + move]
        if target != "0" and (target == " " or target.isupper() == isBlack):
            available_moves.append(index + move)
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
        - 0's represent out of bounds spaces so we can easily identify moves that go out of bounds
        by seeing whether they land on a 0 (this is to avoid having to deal with index errors and stuff)
        '''
        self.board = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                      '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                      '0', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', '0',
                      '0', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', '0',
                      '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0',
                      '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0',
                      '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0',
                      '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0',
                      '0', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '0',
                      '0', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', '0',
                      '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                      '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                      ]
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


    def makeMove(self, piece_index, target_index, special=None):
        # Moves a piece on the board from one position to the other
        # Should only be called after the move is confirmed to be valid
        if special is None:
            self.board[target_index] = self.board[piece_index]
            self.board[piece_index] = ' '
        elif special == "castle":
            # add code to handle castling here
            pass
        elif special == "en passant":
            # add code for en passant here
            pass

if __name__ == "__main__":
    board = Board()
    board.printBoard()

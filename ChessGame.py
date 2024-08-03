# Author: Allison Majors
# GitHub username: birdybird10
# Date: 11/29/23
# Description: This file makes use of three different classes in order to implement a modified
# version of chess. The pieces begin in their traditional squares, and white moves first, but
# the winner is the first player to capture all of an opponent's pieces of one type. The king
# is not a special piece. There is no check, checkmate, castling, en passant, or pawn promotion.
# The pieces all move and capture the same, with pawns still being allowed to move two spaces
# forward on their first move. The three classes involved are 'ChessVar', 'Player', and 'Piece'.
# The ChessVar class has a black player, a white player, and a current player. The ChessVar class
# also has a board which is a list of 8 lists with 8 elements each. The elements are all objects
# of class 'Piece'. ChessVar has a method called 'make_move()' which takes in a square the player
# wants to move from and the square they want to move to and sees if that move is valid. If yes,
# then we move the piece and also make any captures. If the player has won, then we update the
# state of the game as such. At the end of 'make_move()', we set the current player to be the
# opposite color if a valid move was made.

class ChessVar:
    """This class implements a modified game of chess. The pieces begin in their traditional squares,
    and white moves first, but the winner is the first player to capture all of an opponent's pieces
    of one type. The king is not a special piece. There is no check, checkmate, castling, en passant,
    or pawn promotion. The pieces all move and capture the same, with pawns still being allowed to
    move two spaces forward on their first move. The board will have columns of values 'a-h' and rows
    of values '1-8'.

    Data Members:
        - self._board (A list of 8 lists that contain 8 elements each, mimicking a real chess
         board. Each element will be of the type "Piece," which is a class that defines a chess
         piece with a given type and color. )
        - self._game_state (Will initially be set to 'UNFINISHED,' but can have a value of either
        'UNFINISHED', 'WHITE_WON', or 'BLACK_WON')
        - self._white_player (Calls upon the class 'Player'. An object of type 'Player' has a color
        and a dictionary with the quantities of pieces that player has captured. Having a white player
        makes it so we can easily access their dictionary and keep track of if the game's
        white player wins. )
        - self._black_player (Calls upon the class 'Player'. An object of type 'Player' has a color
        and a dictionary with the quantities of pieces that player has captured. Having a black player
        makes it so we can easily access their dictionary and keep track of if the game's
        black player wins.)
        - self._current_player (Will be initially set to self._white_player. Helps to keep track of
        whose turn it is.)
        - self._reference_dict (Will be a dictionary that can be used to translate a given square's
        algebraic notation to its actual row and column indices in self._board. For example: 'a': 0,
        'b':1, '1': 0, '2': 1 and so on.)

    Methods:
        - init method
            - Initializes self._board to mimic a standard chess board setup with 64 pieces of particular
            types in their usual starting spots.
            - Initializes self._game_state to be 'UNFINISHED'.
            - Initializes self._white_player to be Player('white').
            - Initializes self._black_player to be Player('black').
            - Initializes self._current_player to be self._white_player.
            - Initializes self._reference_dict to be the following:
                        {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
                        '1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}.
        - get_game_state(self)
            - Returns the state of the game.
        - set_game_state(self, state)
            - Sets the state of the game to be the given state (string).
        - set_current_player(self, player)
            - Sets the current player to be the player we send it.
        - make_move(self, square_moved_from, square_moved_to)
            - Given a square the player is moving from and the square the player wants to move
            to, this method returns True if the move is valid and False otherwise.
        - is_valid_move_king(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'king' and False otherwise.
        - is_valid_move_queen(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'queen' and False otherwise.
        - is_valid_move_rook(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'rook' and False otherwise.
        - is_valid_move_bishop(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'bishop' and False otherwise.
        - is_valid_move_knight(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'knight' and False otherwise.
        - is_valid_move_pawn(self, column_from, row_from, column_to, row_to)
            - This method is called inside 'make_move' and returns True if a given move is valid
            for a piece of type 'pawn' and False otherwise.
        - validate_coordinates_list(self, coordinates_list, column_from, row_from, column_to, row_to, piece_type)
            - This method is called inside each is_valid_move_(piecetype) method. It sees if
            a specific move can be made for a specific piece, and if so makes the move as well as any
            capture. It returns True if the move was made and False otherwise.
        - display_board(self)
            - Displays the board in an organized manner.
        - check_if_winner(self)
            - Checks if self._current_player has won the game.

    Classes in communication with:
        - Piece (A ChessVar object has a board filled with 64 elements of type 'Piece'.)
        - Player (A ChessVar object has a white player, black player, and a current player being
        either the white or black player.)
    """

    def __init__(self):
        self._board = [[Piece('rook','black'), Piece('knight','black'),
                        Piece('bishop','black'), Piece('queen','black'),
                        Piece('king','black'), Piece('bishop','black'),
                        Piece('knight','black'), Piece('rook','black')],
                       [Piece('pawn','black'), Piece('pawn','black'),
                        Piece('pawn','black'), Piece('pawn','black'),
                        Piece('pawn','black'), Piece('pawn','black'),
                        Piece('pawn','black'), Piece('pawn','black')],
                       [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
                       [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
                       [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
                       [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()],
                       [Piece('pawn','white'), Piece('pawn','white'),
                        Piece('pawn','white'), Piece('pawn','white'),
                        Piece('pawn','white'), Piece('pawn','white'),
                        Piece('pawn','white'), Piece('pawn','white')],
                       [Piece('rook','white'), Piece('knight','white'),
                        Piece('bishop','white'), Piece('queen','white'),
                        Piece('king','white'), Piece('bishop','white'),
                        Piece('knight','white'), Piece('rook','white')]]
        self._game_state = 'UNFINISHED'
        self._white_player = Player('white')
        self._black_player = Player('black')
        self._current_player = self._white_player
        # This dictionary is used to translate a given square's algebraic notation to its actual
        # row and column indices in self._board.
        self._reference_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,
                                '1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}

    def get_game_state(self):
        """
        Returns the state of the game.
        Return value:
            'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        return self._game_state

    def set_game_state(self, state):
        """
        Sets the game state to be 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        Parameters:
            - state: will be either 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        self._game_state = state

    def set_current_player(self, player):
        """
        Sets the current player to be the class's black player or white player.
        Parameters:
            - player: will be either self._white_player or self._black_player
        """
        self._current_player = player

    def make_move(self, square_moved_from, square_moved_to):
        """
        Given a starting square and an ending square, this method returns True if that move can
        be made and returns False otherwise. If the piece being moved does not match the current
        player's color, we return False. If a piece does not exist in square_moved_from, we return
        False. If the game has already been won, we return False. If a capture was made, we update
        the board accordingly as well as the player's 'captured_pieces' dictionary. If the move
        being made causes the player to win, then we update the state of the game. Then we change
        whose turn it is and return True since a valid move has been made.

        Parameters:
            - square_moved_from: A string in algebraic notation that represents the square on the
            chess board that the player wants to start at. Example: 'a1'
            - square_moved_to: A string in algebraic notation that represents the square on the
            chess board that the player wants to move a piece to. Example: 'b3'

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid and nothing occurs
        """

        # first get the row and column indices of the square the player wants to move a piece from
        char_from1 = square_moved_from[0]
        char_from2 = square_moved_from[1]
        column_from = self._reference_dict[char_from1]
        row_from = self._reference_dict[char_from2]

        # get the row and column indices of the square moving to
        char_to1 = square_moved_to[0]
        char_to2 = square_moved_to[1]
        column_to = self._reference_dict[char_to1]
        row_to = self._reference_dict[char_to2]

        # get the specific piece being moved
        piece_being_moved = self._board[row_from][column_from]

        # boolean for if a valid move is eventually made or not
        move_was_made = False

        # make sure a piece is in the square we are moving from
        if piece_being_moved.get_type() == '':
            return False

        # make sure the piece being moved matches the current player's color
        if piece_being_moved.get_color() != self._current_player.get_color():
            return False

        # check status of game, must be unfinished to make a move
        if self._game_state != "UNFINISHED":
            return False

        # Based on the type of the piece, call the method that checks if that piece can
        # be moved to its desired square or not. If the move is valid, 'move_was_made'
        # will be set to True.
        if piece_being_moved.get_type() == 'king':
            king_can_move = self.is_valid_move_king(column_from, row_from, column_to, row_to)
            move_was_made = king_can_move

        elif piece_being_moved.get_type() == 'queen':
            queen_can_move = self.is_valid_move_queen(column_from, row_from, column_to, row_to)
            move_was_made = queen_can_move

        elif piece_being_moved.get_type() == 'rook':
            rook_can_move = self.is_valid_move_rook(column_from, row_from, column_to, row_to)
            move_was_made = rook_can_move

        elif piece_being_moved.get_type() == 'bishop':
            bishop_can_move = self.is_valid_move_bishop(column_from, row_from, column_to, row_to)
            move_was_made = bishop_can_move

        elif piece_being_moved.get_type() == 'knight':
            knight_can_move = self.is_valid_move_knight(column_from, row_from, column_to, row_to)
            move_was_made = knight_can_move

        elif piece_being_moved.get_type() == 'pawn':
            pawn_can_move = self.is_valid_move_pawn(column_from, row_from, column_to, row_to)
            move_was_made = pawn_can_move

        # the move the player wanted to make is not valid, return False
        if not move_was_made:
            return False

        # check if the current player has won, if yes then update the state of the game
        won = self.check_if_winner()
        if won:
            if self._current_player.get_color() == 'white':
                self.set_game_state('WHITE_WON')
            else:
                self.set_game_state('BLACK_WON')

        # a valid move has been made, so change player
        if self._current_player == self._white_player:
            self.set_current_player(self._black_player)
        else:
            self.set_current_player(self._white_player)

        # a valid move was made, return True
        return True


    def is_valid_move_king(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a King can make that move and returns False otherwise. We use the different movements
        of a King to create a list of all the possible coordinates on the board the King could
        move to. (A King can move one square in any direction). Then, we send this list of
        coordinates to the method 'self.validate_coordinates_list()' to see if the specific move
        we want our King to make is valid.

        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid coordinates
        coordinates_list =[]

        # check that all moves keep us on the board
        # horizontal move left
        if 0<=column_from-1<=7:
            coordinates_list.append((row_from,column_from-1))
        # horizontal move right
        if 0<=column_from+1<=7:
            coordinates_list.append((row_from,column_from+1))
        # vertical move down
        if 0<=row_from-1<=7:
            coordinates_list.append((row_from-1, column_from))
        # vertical move up
        if 0<=row_from+1<=7:
            coordinates_list.append((row_from+1, column_from))
        # diagonal move
        if 0<=column_from-1<=7 and 0<=row_from-1<=7:
            coordinates_list.append((row_from-1, column_from-1))
        # diagonal move
        if 0<=column_from-1<=7 and 0<=row_from+1<=7:
            coordinates_list.append((row_from+1, column_from-1))
        # diagonal move
        if 0<=column_from+1<=7 and 0<=row_from+1<=7:
            coordinates_list.append((row_from+1, column_from+1))
        # diagonal move
        if 0<=column_from+1<=7 and 0<=row_from-1<=7:
            coordinates_list.append((row_from-1, column_from+1))

        return self.validate_coordinates_list(coordinates_list, column_from, row_from, column_to, row_to, 'king')



    def is_valid_move_queen(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a Queen can make that move and returns False otherwise. We use the different movements
        of a Queen to create a list of all the possible coordinates on the board the Queen could
        move to. (A queen can move any direction any number of spaces). Then, we send this list
        of coordinates to the method 'self.validate_coordinates_list()' to see if the specific
        move we want our Queen to make is valid.

        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid coordinates
        coordinates_list = []

        # horizontal moves going left
        move = column_from - 1
        # stay in bounds
        while 0 <= move <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[row_from][move].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[row_from][move].get_color() != self._current_player.get_color()
                  and self._board[row_from][move].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((row_from, move))
                break
            # add coordinate to list
            coordinates_list.append((row_from, move))
            move -= 1

        # horizontal moves going right
        move2 = column_from + 1
        # stay in bounds
        while 0 <= move2 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[row_from][move2].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[row_from][move2].get_color() != self._current_player.get_color()
                  and self._board[row_from][move2].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((row_from, move2))
                break
            # add coordinate to list
            coordinates_list.append((row_from, move2))
            move2 += 1

        # vertical moves going up
        move3 = row_from - 1
        # stay in bounds
        while 0 <= move3 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move3][column_from].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move3][column_from].get_color() != self._current_player.get_color()
                  and self._board[move3][column_from].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move3, column_from))
                break
            # add coordinate to list
            coordinates_list.append((move3, column_from))
            move3 -= 1

        # vertical moves going down
        move4 = row_from + 1
        # stay in bounds
        while 0 <= move4 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move4][column_from].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move4][column_from].get_color() != self._current_player.get_color()
                  and self._board[move4][column_from].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move4, column_from))
                break
            # add coordinate to list
            coordinates_list.append((move4, column_from))
            move4 += 1

        # left top diagonal moves
        move5y = column_from-1
        move5x = row_from-1
        # stay in bounds
        while 0<=move5y<=7 and 0<=move5x<=7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move5x][move5y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move5x][move5y].get_color() != self._current_player.get_color()
                  and self._board[move5x][move5y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move5x, move5y))
                break
            coordinates_list.append((move5x, move5y))
            move5y -= 1
            move5x -= 1

        # left bottom diagonal moves
        move6y = column_from - 1
        move6x = row_from + 1
        # stay in bounds
        while 0 <= move6y <= 7 and 0 <= move6x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move6x][move6y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move6x][move6y].get_color() != self._current_player.get_color()
                  and self._board[move6x][move6y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move6x, move6y))
                break
            coordinates_list.append((move6x, move6y))
            move6y -= 1
            move6x += 1

        # right bottom diagonal moves
        move7y = column_from + 1
        move7x = row_from + 1
        # stay in bounds
        while 0 <= move7y <= 7 and 0 <= move7x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move7x][move7y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move7x][move7y].get_color() != self._current_player.get_color()
                  and self._board[move7x][move7y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move7x, move7y))
                break
            coordinates_list.append((move7x, move7y))
            move7y += 1
            move7x += 1

        # right top diagonal moves
        move8y = column_from + 1
        move8x = row_from - 1
        # stay in bounds
        while 0 <= move8y <= 7 and 0 <= move8x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move8x][move8y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then queen can move there but
            # can't move anymore after that
            elif (self._board[move8x][move8y].get_color() != self._current_player.get_color()
                  and self._board[move8x][move8y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move8x, move8y))
                break
            coordinates_list.append((move8x, move8y))
            move8y += 1
            move8x -= 1

        return self.validate_coordinates_list(coordinates_list, column_from, row_from, column_to, row_to, 'queen')


    def is_valid_move_rook(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a Rook can make that move and returns False otherwise. We use the different movements
        of a Rook to create a list of all the possible coordinates on the board the Rook could
        move to. (A rook can move vertically and horizontally any number of spaces). Then, we
        send this list of coordinates to the method 'self.validate_coordinates_list()' to see
        if the specific move we want our Rook to make is valid.

        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid coordinates
        coordinates_list = []

        # horizontal moves going left
        move = column_from - 1
        # stay in bounds
        while 0 <= move <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[row_from][move].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then rook can move there but
            # can't move anymore after that
            elif (self._board[row_from][move].get_color() != self._current_player.get_color()
                  and self._board[row_from][move].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((row_from, move))
                break
            # add coordinate to list
            coordinates_list.append((row_from, move))
            move -= 1

        # horizontal moves going right
        move2 = column_from + 1
        # stay in bounds
        while 0 <= move2 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[row_from][move2].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then rook can move there but
            # can't move anymore after that
            elif (self._board[row_from][move2].get_color() != self._current_player.get_color()
                  and self._board[row_from][move2].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((row_from, move2))
                break
            # add coordinate to list
            coordinates_list.append((row_from, move2))
            move2 += 1

        # vertical moves going up
        move3 = row_from - 1
        # stay in bounds
        while 0 <= move3 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move3][column_from].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then rook can move there but
            # can't move anymore after that
            elif (self._board[move3][column_from].get_color() != self._current_player.get_color()
                  and self._board[move3][column_from].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move3, column_from))
                break
            # add coordinate to list
            coordinates_list.append((move3, column_from))
            move3 -= 1

        # vertical moves going down
        move4 = row_from + 1
        # stay in bounds
        while 0 <= move4 <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move4][column_from].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then rook can move there but
            # can't move anymore after that
            elif (self._board[move4][column_from].get_color() != self._current_player.get_color()
                  and self._board[move4][column_from].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move4, column_from))
                break
            # add coordinate to list
            coordinates_list.append((move4, column_from))
            move4 += 1

        return self.validate_coordinates_list(coordinates_list, column_from, row_from, column_to, row_to, 'rook')

    def is_valid_move_bishop(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a Bishop can make that move and returns False otherwise. We use the different movements
        of a Bishop to create a list of all the possible coordinates on the board the Bishop could
        move to. (A bishop can move any diagonal direction any number of spaces). Then, we send this
        list of coordinates to the method 'self.validate_coordinates_list()' to see if the specific
        move we want our Bishop to make is valid.

        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid coordinates
        coordinates_list = []

        # left top diagonal moves
        move5y = column_from - 1
        move5x = row_from - 1
        # stay in bounds
        while 0 <= move5y <= 7 and 0 <= move5x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move5x][move5y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then bishop can move there but
            # can't move anymore after that
            elif (self._board[move5x][move5y].get_color() != self._current_player.get_color()
                  and self._board[move5x][move5y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move5x, move5y))
                break
            coordinates_list.append((move5x, move5y))
            move5y -= 1
            move5x -= 1

        # left bottom diagonal moves
        move6y = column_from - 1
        move6x = row_from + 1
        # stay in bounds
        while 0 <= move6y <= 7 and 0 <= move6x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move6x][move6y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then bishop can move there but
            # can't move anymore after that
            elif (self._board[move6x][move6y].get_color() != self._current_player.get_color()
                  and self._board[move6x][move6y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move6x, move6y))
                break
            coordinates_list.append((move6x, move6y))
            move6y -= 1
            move6x += 1

        # right bottom diagonal moves
        move7y = column_from + 1
        move7x = row_from + 1
        # stay in bounds
        while 0 <= move7y <= 7 and 0 <= move7x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move7x][move7y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then bishop can move there but
            # can't move anymore after that
            elif (self._board[move7x][move7y].get_color() != self._current_player.get_color()
                  and self._board[move7x][move7y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move7x, move7y))
                break
            coordinates_list.append((move7x, move7y))
            move7y += 1
            move7x += 1

        # right top diagonal moves
        move8y = column_from + 1
        move8x = row_from - 1
        # stay in bounds
        while 0 <= move8y <= 7 and 0 <= move8x <= 7:
            # check if run into piece of same color, if yes then can't move any more spaces that particular direction
            if self._board[move8x][move8y].get_color() == self._current_player.get_color():
                break
            # check if run into piece of opposite color, if yes then bishop can move there but
            # can't move anymore after that
            elif (self._board[move8x][move8y].get_color() != self._current_player.get_color()
                  and self._board[move8x][move8y].get_color() != ''):
                # add coordinate to list
                coordinates_list.append((move8x, move8y))
                break
            coordinates_list.append((move8x, move8y))
            move8y += 1
            move8x -= 1

        return self.validate_coordinates_list(coordinates_list, column_from, row_from, column_to, row_to, 'bishop')


    def is_valid_move_knight(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a Knight can make that move and returns False otherwise. We use the different movements
        of a Knight to create a list of all the possible coordinates on the board the Knight could
        move to. (A knight can move in an 3 square 'L' shape 8 different ways and can jump over
        other pieces). Then, we send this list of coordinates to the method
        'self.validate_coordinates_list()' to see if the specific move we want our Knight to make
        is valid. We keep in mind that a Knight can jump over other pieces.

        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid coordinates
        coordinates_list = []

        # move forward two and to the left 1
        move1y = column_from - 1
        move1x = row_from - 2
        # stay in bounds
        if 0 <= move1y <= 7 and 0 <= move1x <= 7:
            coordinates_list.append((move1x, move1y))

        # move forward two and to the right 1
        move2y = column_from + 1
        move2x = row_from - 2
        # stay in bounds
        if 0 <= move2y <= 7 and 0 <= move2x <= 7:
            coordinates_list.append((move2x, move2y))

        # move backwards two and to the left 1
        move3y = column_from - 1
        move3x = row_from + 2
        # stay in bounds
        if 0 <= move3y <= 7 and 0 <= move3x <= 7:
            coordinates_list.append((move3x, move3y))

        # move backwards two and to the right 1
        move4y = column_from + 1
        move4x = row_from + 2
        # stay in bounds
        if 0 <= move4y <= 7 and 0 <= move4x <= 7:
            coordinates_list.append((move4x, move4y))

        # move forward 1 and to the left 2
        move5y = column_from - 2
        move5x = row_from - 1
        # stay in bounds
        if 0 <= move5y <= 7 and 0 <= move5x <= 7:
            coordinates_list.append((move5x, move5y))

        # move forward 1 and to the right 2
        move6y = column_from + 2
        move6x = row_from - 1
        # stay in bounds
        if 0 <= move6y <= 7 and 0 <= move6x <= 7:
            coordinates_list.append((move6x, move6y))

        # move backwards 1 and to the left 2
        move7y = column_from - 2
        move7x = row_from + 1
        # stay in bounds
        if 0 <= move7y <= 7 and 0 <= move7x <= 7:
            coordinates_list.append((move7x, move7y))

        # move backwards 1 and to the right 2
        move8y = column_from + 2
        move8x = row_from + 1
        # stay in bounds
        if 0 <= move8y <= 7 and 0 <= move8x <= 7:
            coordinates_list.append((move8x, move8y))

        return self.validate_coordinates_list(coordinates_list, column_from, row_from, column_to, row_to, 'knight')


    def is_valid_move_pawn(self, column_from, row_from, column_to, row_to):
        """
        Given a starting column and row and an ending column and row, this method returns True
        if a Pawn can make that move and returns False otherwise. We use the different movements
        of a Pawn to create a list of all the possible coordinates on the board the Pawn could
        move to. A pawn is different than the other pieces because it can move forward two squares
        on its first turn, but only one square otherwise. It also captures pieces diagonally instead
        of forwards. Therefore, we create another list of all the possible coordinates on the board
        the Pawn could move to if it is making a capture, since that would be a diagonal move. Then,
        we see if the square the player wants to move to is in one of the coordinates lists. Then,
        we make sure another piece is not in the square already if the pawn is just making a move.
        If the pawn is capturing another piece, we make sure that piece is of the opposite color.
        If a move or capture is made, we update the board accordingly as well as the player's
        'captured_pieces_dictionary'.


        Parameters:
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # list of valid moves
        coordinates_list_for_move = []

        # list of valid capture moves
        coordinates_list_for_capture = []

        # check if color is black or white
        current_color = self._current_player.get_color()

        # get possible white moves
        if current_color == 'white':
            # check if it is the pawn's first turn, if yes then moving forward two spaces is valid
            if row_from == 6:
                coordinates_list_for_move.append((row_from - 2, column_from))
            # normal move one square forward
            if 0 <= row_from - 1 <= 7:
                coordinates_list_for_move.append((row_from - 1, column_from))
            # check top left diagonal for piece of opposite color
            if 0 <= row_from-1 <= 7 and 0 <= column_from-1 <= 7:
                left_diagonal_piece = self._board[row_from-1][column_from-1]
                if left_diagonal_piece.get_color() == 'black':
                    coordinates_list_for_capture.append((row_from-1, column_from-1))
            # check top right diagonal for piece of opposite color
            if 0 <= row_from-1 <= 7 and 0 <= column_from+1 <= 7:
                right_diagonal_piece = self._board[row_from-1][column_from+1]
                if right_diagonal_piece.get_color() == 'black':
                    coordinates_list_for_capture.append((row_from-1, column_from+1))

        # get possible black moves
        elif current_color == 'black':
            # check if it is the pawn's first turn, if yes then moving forward two spaces is valid
            if row_from == 1:
                coordinates_list_for_move.append((row_from + 2, column_from))
            # normal move one square forward
            if 0 <= row_from + 1 <= 7:
                coordinates_list_for_move.append((row_from + 1, column_from))
            # check top left diagonal for piece of opposite color
            if 0 <= row_from + 1 <= 7 and 0 <= column_from - 1 <= 7:
                left_diagonal_piece = self._board[row_from + 1][column_from - 1]
                if left_diagonal_piece.get_color() == 'white':
                    coordinates_list_for_capture.append((row_from + 1, column_from - 1))
            # check top right diagonal for piece of opposite color
            if 0 <= row_from + 1 <= 7 and 0 <= column_from + 1 <= 7:
                right_diagonal_piece = self._board[row_from + 1][column_from + 1]
                if right_diagonal_piece.get_color() == 'white':
                    coordinates_list_for_capture.append((row_from + 1, column_from + 1))

        # check if square we want to move to is in our coordinates list
        if (row_to, column_to) in coordinates_list_for_move:
            # now check if a piece of either the same color or opposite is in that square
            piece = self._board[row_to][column_to]
            if piece.get_color() != '':
                # can't move forward
                return False
            else:
                # move piece to desired square
                self._board[row_to][column_to] = Piece('pawn', current_color)
                # make previous spot empty
                self._board[row_from][column_from] = Piece()

        # need to check if we made a capture or not, rowto and columnto piece will be
        # of opposite color in that case
        elif (row_to,column_to) in coordinates_list_for_capture:
            # capture and replace piece
            captured_piece = self._board[row_to][column_to]
            # add to captured dictionary
            if current_color == 'white':
                self._white_player.add_captured_piece(captured_piece.get_type())
            else:
                self._black_player.add_captured_piece(captured_piece.get_type())
            # replace piece
            self._board[row_to][column_to] = Piece('pawn', current_color)
            # make previous spot empty
            self._board[row_from][column_from] = Piece()

        # move not valid
        else:
            return False

        return True

    def validate_coordinates_list(self, coordinates_list, column_from, row_from, column_to, row_to, piece_type):
        """
        Given a list of valid coordinates for potential moves of a piece, this method determines
        if the move the player wants to make is valid. First, the square the player wants to move
        to must exist in the coordinates list. Then, we check if a piece of the same color exists
        in the square. If so, we return False. Then, we check if a piece of the opposite color
        exists in that square. If so, then we are making a capture, so we update the current player's
        captured_pieces_dictionary. Then we update the board by moving our piece to its desired
        square and removing any captured piece.
        * this method does not apply to pawns because pawns move and capture differently

        Parameters:
            - coordinates_list: A list of valid coordinates (tuples) for potential moves of a piece.
            - column_from: An integer that represents the column list index of the square on the
            chess board that the player wants to start at. Example: 0
            - row_from: An integer that represents the row list index of the square on the
            chess board that the player wants to start at. Example: 0
            - column_to: An integer that represents the column list index of the square on the
            chess board that the player wants to move to. Example: 0
            - row_to: An integer that represents the row list index of the square on the
            chess board that the player wants to move to. Example: 0
            - piece_type: A string that represents the type of piece we are moving.

        Return value:
            - True: if a valid move was made
            - False: if the move is not valid
        """

        # first check if square want to move to is in our coordinates_list
        if (row_to, column_to) in coordinates_list:
            # now check if a piece of the same color is in that square
            captured_piece = self._board[row_to][column_to]
            if captured_piece.get_color() == self._current_player.get_color():
                return False
            # now check if opposite color piece is there- then capture
            else:
                # add to captured dictionary
                if self._current_player.get_color() == 'white':
                    if self._board[row_to][column_to].get_type() != '':
                        self._white_player.add_captured_piece(captured_piece.get_type())
                else:
                    if self._board[row_to][column_to].get_type() != '':
                        self._black_player.add_captured_piece(captured_piece.get_type())
                # replace piece
                self._board[row_to][column_to] = Piece(piece_type, self._current_player.get_color())
                # make previous spot empty
                self._board[row_from][column_from] = Piece()
        # not a valid move
        else:
            return False
        # move was valid
        return True


    def display_board(self):
        """
        This method prints the chess board. A '*' character represents a blank square.
        A dashed line is included at the bottom.
        """
        for row in self._board:
            for piece in row:
                # print a '*' for an empty square
                if piece.get_type() == '':
                    print(f"{'*':<12}",end='')
                # print the piece color with its type
                else:
                    print(f"{piece.get_color():<5}{piece.get_type():<6}",end=" ")
            print()
        # separating line
        print('-'*96)

    def check_if_winner(self):
        """This method will access the captured_pieces_dictionary of the current player and see
        if all the pieces of one type have been captured. If yes, return True, if no, return False.

        Return value:
            - True if the current player has won
            - False if the current player has not won
        """

        # iterate through player's dictionary of captured pieces
        for key, value in self._current_player.get_captured_pieces().items():
            # all rooks, knights, or bishops have been captured
            if key == 'rook' or key == 'knight' or key == 'bishop':
                if value == 2:
                    return True
            # all queens or kings have been captured
            elif key == 'queen' or key == 'king':
                if value == 1:
                    return True
            # all pawns have been captured
            else:
                if value == 8:
                    return True

        return False

class Piece:
    """
    This class defines an object of type 'Piece'. A piece exists on the board in a
    chess game (ChessVar). A piece has a type and a color.

    Data members:
        - self._type (a piece can be a 'rook', 'bishop', 'king', 'queen', 'knight',
        or 'pawn')
        - self._color (either black or white)

    Methods:
        - get_type()
            - This method returns the type of the piece.
        - get_color()
            - This method returns the color of the piece.

    Classes in communication with:
        - The ChessVar class has many instances where it might need to instantiate a
        chess piece. The board in a ChessVar object contains pieces of various types.
        These pieces move and get captured throughout a game.
    """

    def __init__(self,type='',color=''):
        self._type = type
        self._color = color

    def get_type(self):
        """
        Returns the type of the piece.

        Return value:
            - piece type (a string being either 'king', 'queen', 'rook', 'bishop',
            'knight', or 'pawn')
        """
        return self._type

    def get_color(self):
        """
        Returns the color of the piece.

        Return value:
            - piece color (a string being either 'black' or 'white')
        """
        return self._color


class Player:
    """
    This class defines an object of type 'Player'. A player exists in a chess game (ChessVar)
    and has a color as well as a dictionary containing the quantities of pieces captured.

    Data members:
        - self._color (A player will either be black or white)
        - self._captured_pieces (A dictionary where each key is a piece type and each value
        is the corresponding number of captured pieces of that type.)

    Methods:
        - get_color(self)
            - This method returns the player's color.
        - get_captured_pieces(self)
            - This method returns the player's dictionary of captured pieces.
        - add_captured_piece(self, type)
            - This method takes in a piece type (string) and uses that to find the same type
            in the keys of self._captured_pieces and increments the corresponding value by 1.

    Classes in communication with:
        - The ChessVar class has a white player, a black player, and a current player
        as data members.
    """

    def __init__(self, color=''):
        self._color = color
        self._captured_pieces = {'rook':0, 'knight':0, 'bishop':0, 'queen':0, 'king':0, 'pawn':0}

    def get_color(self):
        """
        Returns the color of the player

        Return value:
            - player color (a string being either 'black' or 'white')
        """
        return self._color
    def get_captured_pieces(self):
        """
        Returns the player's dictionary of captured pieces.

        Return value:
            - self._captured_pieces (dictionary)
        """
        return self._captured_pieces
    def add_captured_piece(self, type):
        """
        This method takes in a piece type (string) and uses that to find the same type
        in the keys of self._captured_pieces and increments the corresponding value by 1.

        Parameters:
             - type (a string being either 'king', 'queen', 'rook', 'bishop',
            'knight', or 'pawn')
        """

        self._captured_pieces[type] += 1


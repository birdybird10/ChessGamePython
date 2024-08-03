# ChessGamePython

This file makes use of three different classes in order to implement a modified
version of chess. The pieces begin in their traditional squares, and white moves first, but
the winner is the first player to capture all of an opponent's pieces of one type. The king
is not a special piece. There is no check, checkmate, castling, en passant, or pawn promotion.
The pieces all move and capture the same, with pawns still being allowed to move two spaces
forward on their first move. The three classes involved are 'ChessVar', 'Player', and 'Piece'.
The ChessVar class has a black player, a white player, and a current player. The ChessVar class
also has a board which is a list of 8 lists with 8 elements each. The elements are all objects
of class 'Piece'. ChessVar has a method called 'make_move()' which takes in a square the player
wants to move from and the square they want to move to and sees if that move is valid. If yes,
then we move the piece and also make any captures. If the player has won, then we update the
state of the game as such. At the end of 'make_move()', we set the current player to be the
opposite color if a valid move was made.

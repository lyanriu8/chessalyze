"""Chess"""

from abc import ABC, abstractmethod
import re
from exceptions.chess_exceptions import InvalidMoveException

class Chess:
    """Represents a game of chess"""

    def __init__(self, white_player_name, black_player_name):
        """Constructor

        Args:
            white_player (str): name of white player
            black_player (str): name of black player
        """
        self.white_player = white_player_name
        self.wp_captured = []

        self.black_player = black_player_name
        self.bp_captured = []
        self.board = Board()
        # finish later


class Board:
    """Represents a chess board"""

    def __init__(self):
        """Constructor"""

        self.log = []
        self.to_move = 0  # 0 means white to move, 1 means black to move
        self.init_pieces()

    def init_pieces(self):
        """Initializes pieces"""
        br_1 = Rook(0, 0)
        bk_1 = Knight(1, 0)
        bb_1 = Bishop(2, 0)
        bq = Queen(3, 0)
        bk = King(4, 0)
        bb_2 = Bishop(5, 0)
        bk_2 = Knight(6, 0)
        br_2 = Rook(7, 0)
        bp_1 = BlackPawn(0, 1)
        bp_2 = BlackPawn(1, 1)
        bp_3 = BlackPawn(2, 1)
        bp_4 = BlackPawn(3, 1)
        bp_5 = BlackPawn(4, 1)
        bp_6 = BlackPawn(5, 1)
        bp_7 = BlackPawn(6, 1)
        bp_8 = BlackPawn(7, 1)
        self.black_pieces = [br_1, bk_1, bb_1, bq, bk, bb_2, bk_2, br_2,
                             bp_1, bp_2, bp_3, bp_4, bp_5, bp_6, bp_7, bp_8]

        wr_1 = Rook(0, 7)
        wk_1 = Knight(1, 7)
        wb_1 = Bishop(2, 7)
        wq = Queen(3, 7)
        wk = King(4, 7)
        wb_2 = Bishop(5, 7)
        wk_2 = Knight(6, 7)
        wr_2 = Rook(7, 7)
        wp_1 = WhitePawn(0, 6)
        wp_2 = WhitePawn(1, 6)
        wp_3 = WhitePawn(2, 6)
        wp_4 = WhitePawn(3, 6)
        wp_5 = WhitePawn(4, 6)
        wp_6 = WhitePawn(5, 6)
        wp_7 = WhitePawn(6, 6)
        wp_8 = WhitePawn(7, 6)
        self.white_pieces = [wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8,
                             wr_1, wk_1, wb_1, wq, wk, wb_2, wk_2, wr_2]

        self.board = [[br_1, bk_1, bb_1, bq, bk, bb_2, bk_2, br_2],
                      [bp_1, bp_2, bp_3, bp_4, bp_5, bp_6, bp_7, bp_8],
                      [None for _ in range(8)],
                      [None for _ in range(8)],
                      [None for _ in range(8)],
                      [None for _ in range(8)],
                      [wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8],
                      [wr_1, wk_1, wb_1, wq, wk, wb_2, wk_2, wr_2]]

    def move(self, move_code):
        """Moves piece if move is valid

        Args:
            intsruction (int): Move code
        """

        from_x = move_code[0]
        from_y = move_code[1]

        to_x = move_code[2]
        to_y = move_code[3]

        if self.board[to_y][to_x] is not None:
            raise InvalidMoveException()

        piece = self.board[from_y][from_x]
        piece.move(to_x, to_y)
        self.board[from_y][from_x] = None
        self.board[to_y][to_x] = piece

        self.to_move = 1 - self.to_move

    def capture(self, move_code):
        """_summary_

        Args:
            move_code (_type_): _description_
        """

        from_x = move_code[0]
        from_y = move_code[1]

        to_x = move_code[2]
        to_y = move_code[3]

        if self.board[to_y][to_x] is not None:
            raise InvalidMoveException()

        piece = self.board[from_y][from_x]
        captured_piece = self.board[to_y][to_x]
        self.board[to_y][to_x] = None

        piece.move(to_x, to_y)
        self.board[from_y][from_x] = None
        self.board[to_y][to_x] = piece

        self.switch_turn()

    def switch_turn(self):
        """Switches turn
        """
        self.to_move = 1 - self.to_move

    def pawn_move(self, move):

        first = move[0]

        if len(move) == 2:
            new_x = self.convert_letter_to_x_coord(move[0])
            new_y = self.convert_num_to_y_coord(move[1])

            # Checks if move is blocked
            for piece in self.white_pieces:
                if piece.x == new_x and piece.y == new_y:
                    raise InvalidMoveException()

            for piece in self.black_pieces:
                if piece.x == new_x and piece.y == new_y:
                    raise InvalidMoveException()

            # Moves pawn on correct file
            if self.to_move == 0:
                for piece in self.white_pieces:
                    if piece.x == new_x and isinstance(piece, Pawn):
                        # will throw an exception if move is invalid
                        self.board[piece.y][piece.x] = None
                        piece.move(new_x, new_y)
                        self.board[new_y][new_x] = piece
                        break

            elif self.to_move == 1:
                for piece in self.black_pieces:
                    if piece.x == new_x and isinstance(piece, Pawn):
                        # will throw an exception if move is invalid
                        self.board[piece.y][piece.x] = None
                        piece.move(new_x, new_y)
                        self.board[new_y][new_x] = piece
                        break

        elif first == "x":
            new_x = self.convert_letter_to_x_coord(move[1])
            new_y = self.convert_num_to_y_coord(move[2])

            if not self.square_free(new_x, new_y):
                raise InvalidMoveException()

            if not self.can_capture(new_x, new_y):
                raise InvalidMoveException()

            self

    def knight_move(self, move):
        pass

    def bishop_move(self, move):
        pass

    def rook_move(self, move):
        pass

    def queen_move(self, move):
        pass

    def king_move(self, move):
        pass

    def castle(self, move):
        pass

    def is_move_proper(self, move):
        """Determines if move is valid

        Args:
            move (str): move instruction

        Returns:
            bool: true if move is valid, else false
        """
        valid_move = r"^(O-O(-O)?|" \
            r"([KQRBN]?([a-h]?[1-8]?))?" \
            r"x?" \
            r"[a-h][1-8]" \
            r"(= [QRBN])?" \
            r"[+#]?)$"

        match = re.match(valid_move, move)

        if match is None:
            return False
        else:
            return True

    def convert_letter_to_x_coord(self, letter):
        """Converts chess letter instruction to coord

        Args:
            letter (char): chess letter representing x-coord

        Returns:
            int: x-coord of letter on board
        """
        return ord(letter) - ord('a')

    def convert_num_to_y_coord(self, num):
        """Converts chess num to coord

        Args:
            num (int): chess num representing y-coord

        Returns:
            int: y-coord of num on board
        """

        return 8 - int(num)

    def square_free(self, new_x, new_y):
        """Checks if square is free

        Args:
            new_x (int): new x-coord
            new_y (int): new y-coord

        Returns:
            bool: true if square is empty, else false
        """

        if self.to_move == 0:
            for piece in self.white_pieces:
                if piece.x == new_x and piece.y == new_y:
                    return False

        elif self.to_move == 1:
            for piece in self.black_pieces:
                if piece.x == new_x and piece.y == new_y:
                    return False

        else:
            return True

    def can_capture(self, new_x, new_y):
        """Determines if piece can be captured

        Args:
            new_x (int): x-coord of capture
            new_y (int): y-coord of capture

        Returns:
            bool: returns true if can capture, else false
        """
        if self.to_move == 0:
            for piece in self.black_pieces:
                if piece.x == new_x and piece.y == new_y:
                    return True

            return False

        else:
            for piece in self.white_pieces:
                if piece.x == new_x and piece.y == new_y:
                    return True

            return False

    def process_move(self, new_x, new_y):
        if self.to_move == 0:
            for piece in self.white_pieces:
                if piece.x == new_x and isinstance(piece, Pawn):
                    # will throw an exception if move is invalid
                    self.board[piece.y][piece.x] = None
                    piece.move(new_x, new_y)
                    self.board[new_y][new_x] = piece
                    break

        elif self.to_move == 1:
            for piece in self.black_pieces:
                if piece.x == new_x and isinstance(piece, Pawn):
                    # will throw an exception if move is invalid
                    self.board[piece.y][piece.x] = None
                    piece.move(new_x, new_y)
                    self.board[new_y][new_x] = piece
                    break

    def print_board(self):
        """Prints board"""

        for x_list in self.board:
            rank = ""
            for piece in x_list:
                if piece is None:
                    rank += ". "
                else:
                    rank += f"{piece.name} "
            print(rank)


class Piece(ABC):
    """Represents a chess piece"""

    def __init__(self, x, y):
        """Contructor for piece object

        Args:
            x (int): x position of piece
            y (int): y position of piece
        """
        self.log = [f"{x}, {y}"]
        self.name = ""
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        """Moves piece to new location if valid

        Args:
            new_x (int): new x position
            new_y (int): new y position
        """
        if self.move_is_valid(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.log.append(f"{new_x}, {new_y}")
        else:
            raise InvalidMoveException()

    @abstractmethod
    def move_is_valid(self, new_x, new_y):
        """Determines if move is valid

        Args:
            new_x (int): new x position
            new_y (int): new y position

        Returns:
            bool: true if move is valid, else false
        """

    def in_bounds(self, new_x, new_y):
        """Determines if move is in bounds

        Args:
            x (int): x position
            y (int): y position

        Returns:
            bool: true if in bounds, else false
        """
        return ((0 <= new_x <= 7) and (0 <= new_y <= 7))


class Pawn(Piece):
    """Represents a pawn"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "p"
        self.points = 1

    def can_two_square_move(self):
        """Determines if pawn can two-square-move

        Returns:
            bool: true if pawn can two-aquare-move, else false
        """
        return len(self.log) == 1


class WhitePawn(Pawn):
    """Represents a white pawn"""

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                (((new_x == self.x) and (new_y == self.y - 1)) or
                 ((new_x == self.x + 1) and (new_y == self.y - 1)) or
                 ((new_x == self.x - 1) and (new_y == self.y - 1)) or
                 ((new_x == self.x) and (new_y == self.y - 2) and self.can_two_square_move())))


class BlackPawn(Pawn):
    """Represents a white pawn"""

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                (((new_x == self.x) and (new_y == self.y + 1)) or
                 ((new_x == self.x + 1) and (new_y == self.y + 1)) or
                 ((new_x == self.x - 1) and (new_y == self.y + 1)) or
                 ((new_x == self.x) and (new_y == self.y + 2) and self.can_two_square_move())))


class Knight(Piece):
    """Represents a knight"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "N"
        self.points = 3

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                (((new_x == self.x + 2) and (new_y == self.y + 1)) or
                 ((new_x == self.x + 2) and (new_y == self.y - 1)) or
                 ((new_x == self.x - 2) and (new_y == self.y + 1)) or
                 ((new_x == self.x - 2) and (new_y == self.y - 1)) or
                 ((new_x == self.x + 1) and (new_y == self.y + 2)) or
                 ((new_x == self.x + 1) and (new_y == self.y - 2)) or
                 ((new_x == self.x - 1) and (new_y == self.y + 2)) or
                 ((new_x == self.x - 1) and (new_y == self.y - 2))))


class Bishop(Piece):
    """Represents a bishop"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "B"
        self.points = 3

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                (abs(self.x - new_x) == abs(self.y - new_y)))


class Rook(Piece):
    """Represents a rook"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "R"
        self.points = 5

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                ((new_x == self.x) or
                 (new_y == self.y) or
                 (self.can_castle())))

    def can_castle(self):
        """Determines if player can castle

        Returns:
            bool: true if rook can castle, else false
        """
        return len(self.log) == 1


class Queen(Piece):
    """Represents a queen"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Q"
        self.points = 9

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                ((new_x == self.x) or
                 (new_y == self.y) or
                 (abs(self.x - new_x) == abs(self.y - new_y))))


class King(Piece):
    """Represents a king"""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "K"

    def move_is_valid(self, new_x, new_y):
        return ((super().in_bounds(new_x, new_y)) and
                (((new_x == self.x + 1) and (new_y == self.y + 1)) or
                 ((new_x == self.x + 1) and (new_y == self.y)) or
                 ((new_x == self.x + 1) and (new_y == self.y - 1)) or
                 ((new_x == self.x) and (new_y == self.y + 1)) or
                 ((new_x == self.x) and (new_y == self.y - 1)) or
                 ((new_x == self.x - 1) and (new_y == self.y + 1)) or
                 ((new_x == self.x - 1) and (new_y == self.y)) or
                 ((new_x == self.x - 1) and (new_y == self.y - 1)) or
                 (self.can_castle())))

    def can_castle(self):
        """Determines if player can castle

        Returns:
            bool: true if rook can castle, else false
        """
        return len(self.log) == 1


board = Board()
board.move("e4")
board.move("e5")
board.move("f4")
board.print_board()

from Classes.Piece import Piece


class Pawn(Piece):
    def __init__(self, white):
        self.white = white
    name = 'Pawn'
    description = 'The weakest piece of them all. Can move only 1 square forward (two if in starting position), ' \
                  'and can only eat pieces on the next forward diagonal squares.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        if abs(pos_x-victim_x) == 1:
            return str((self.white and victim_y-pos_y == 1) or (not self.white and pos_y-victim_y == 1))
        return 'False'


class King(Piece):
    name = 'King'
    description = 'The most valuable piece. If it can\'t defend or move and is under attack, you lose. ' \
                  'It can move one square in all directions.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        return str(max(abs(pos_x-victim_x), abs(pos_y-victim_y)) <= 1)


class Queen(Piece):
    name = 'Queen'
    description = 'The most powerful piece. It is very valuable so it must be used with care. ' \
                  'Can move diagonally, horizontally and vertically across the board.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        return str(pos_x == victim_x or pos_y == victim_y or abs(pos_x-victim_x) == abs(pos_y-victim_y))


class Knight(Piece):
    name = 'Knight'
    description = 'Piece with the strangest movement. ' \
                  'Can move only in L shapes (3 squares forward, 1 to the side), but in all directions.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        return str(abs(pos_x-victim_x) == 3 and abs(pos_y-victim_y) == 1
                   or abs(pos_y-victim_y) == 3 and abs(pos_x-victim_x) == 1)


class Bishop(Piece):
    name = 'Bishop'
    description = 'Piece of the same value of Knight (or a tiny bit more, if you wish). ' \
                  'Can move only diagonally across the board.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        return str(abs(pos_x-victim_x) == abs(pos_y-victim_y))


class Rook(Piece):
    name = 'Rook'
    description = 'A powerful piece that can move horizontally and vertically across the board.'

    def beats_victim_piece(self, pos_x, pos_y, victim_x, victim_y):
        if pos_y == victim_y and pos_x == victim_x:
            return 'Pieces intersect'
        return str(pos_x == victim_x or pos_y == victim_y)

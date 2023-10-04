class Figure:
    def __init__(self, is_white, x, y):
        self.x = x
        self.y = y
        self.color_is_white = is_white

    def change_color(self):
        self.color_is_white = not self.color_is_white

    def can_move(self, new_x, new_y):
        return 0 <= new_x <= 7 and 0 <= new_y <= 7

    def move(self, new_x, new_y):
        if self.can_move(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def __str__(self):
        return f"{self.__class__.__name__}(Color: {'White' if self.color_is_white else 'Black'}, Position: ({self.x}, {self.y}))"


class Pawn(Figure):
    def can_move(self, new_x, new_y):
        if super().can_move(new_x, new_y) and self.y == new_y:
            if self.color_is_white and new_x == self.x + 1:
                return True
            elif not self.color_is_white and new_x == self.x - 1:
                return True
        return False


class Knight(Figure):
    def move(self, new_x, new_y):
        if super().can_move(new_x, new_y):
            dx = abs(self.x - new_x)
            dy = abs(self.y - new_y)
            if (dx == 2 and dy == 3) or (dx == 3 and dy == 2):
                return True
        return False


class Bishop(Figure):
    def move(self, new_x, new_y):
        if super().can_move(new_x, new_y):
            dx = abs(self.x - new_x)
            dy = abs(self.y - new_y)
            if dx == dy:
                return True
        return False


class Rook(Figure):
    def can_move(self, new_x, new_y):
        if super().can_move(new_x, new_y):
            if self.x == new_x or self.y == new_y:
                return True
        return False


class Queen(Figure):
    def can_move(self, new_x, new_y):
        if super().can_move(new_x, new_y):
            dx = abs(self.x - new_x)
            dy = abs(self.y - new_y)
            if self.x == new_x or self.y == new_y and dx == dy:
                return True
        return False


class King(Figure):
    def can_move(self, new_x, new_y):
        if super().can_move(new_x, new_y):
            dx = abs(self.x - new_x)
            dy = abs(self.y - new_y)
            if dx <= 1 and dy <= 1:
                return True
        return False


def get_valid_moves(figures, new_x, new_y):
    valid_moves = []
    for figure in figures:
        if figure.can_move(new_x, new_y):
            valid_moves.append(figure)
    return valid_moves

my_figure = Pawn(True, 0, 0)
print(my_figure)

new_x = 3
new_y = 1
if my_figure.can_move(new_x, new_y):
    print(f"My {my_figure.__class__} can move ({new_x}, {new_y})")
else:
    print(f"My {my_figure.__class__} cannot move ({new_x}, {new_y})")

from window import Point, Line


class Cell:
    def __init__(
        self,
        x1,
        x2,
        y1,
        y2,
        window
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        if not self._win:
            return

        top_wall_p1 = Point(self._x1, self._y1)
        top_wall_p2 = Point(self._x2, self._y1)
        top_line = Line(top_wall_p1, top_wall_p2)

        if self.has_top_wall:
            self._win.draw_line(top_line, "white")
        else:
            self._win.draw_line(top_line, "black")

        right_wall_p1 = Point(self._x2, self._y1)
        right_wall_p2 = Point(self._x2, self._y2)
        right_line = Line(right_wall_p1, right_wall_p2)

        if self.has_right_wall:
            self._win.draw_line(right_line, "white")
        else:
            self._win.draw_line(right_line, "black")

        left_wall_p1 = Point(self._x1, self._y1)
        left_wall_p2 = Point(self._x1, self._y2)
        left_line = Line(left_wall_p1, left_wall_p2)

        if self.has_left_wall:
            self._win.draw_line(left_line, "white")
        else:
            self._win.draw_line(left_line, "black")

        bottom_wall_p1 = Point(self._x1, self._y2)
        bottom_wall_p2 = Point(self._x2, self._y2)
        bottom_line = Line(bottom_wall_p1, bottom_wall_p2)

        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, "white")
        else:
            self._win.draw_line(bottom_line, "black")

    def draw_move(self, to_cell, undo=False):

        if undo:
            color = "grey"
        else:
            color = "red"

        if not self._win:
            return

        from_center = Point(
            self._x2 - (self._x2 - self._x1) / 2,
            self._y2 - (self._y2 - self._y1) / 2
        )

        to_center = Point(
            to_cell._x2 - (to_cell._x2 - to_cell._x1) / 2,
            to_cell._y2 - (to_cell._y2 - to_cell._y1) / 2
        )

        from_line = Line(from_center, to_center)

        self._win.draw_line(from_line, color)

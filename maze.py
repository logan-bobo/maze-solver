
from cell import Cell

from time import sleep


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._cells = []
        self.create_cells()

    def create_cells(self):
        for col in range(self._num_cols):
            self._cells.append(
                [Cell(0, 0, 0, 0, self._win) for i in range(self._num_rows)]
            )

        x_draw_possition = self._x1
        y_draw_possition = self._y1

        for col in self._cells:
            for cell in col:
                # Set the top left point of the cell
                cell._x1 = x_draw_possition
                cell._y1 = y_draw_possition

                # Set the bottom right possition of the cell
                cell._x2 = x_draw_possition + self._cell_size_x
                cell._y2 = y_draw_possition + self._cell_size_y

                cell.draw()

                self.animate()

                y_draw_possition += self._cell_size_y

            # Reset the Y possition of the draw to start at the
            # top of the next col
            y_draw_possition = self._y1
            x_draw_possition += self._cell_size_x

    def animate(self):
        self._win.redraw()
        sleep(0.05)

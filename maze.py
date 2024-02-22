
from cell import Cell

from time import sleep
from enum import Enum

import random


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window,
        seed=None
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
        self.seed = seed

        if self.seed is not None:
            random.seed(seed)

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

        self.break_entrance_and_exit()
        self.break_walls(0, 0)
        self.reset_cells()
        self.solve()

    def animate(self):
        if not self._win:
            return

        self._win.redraw()
        sleep(0.005)

    def break_entrance_and_exit(self):
        maze_entrance = self._cells[0][0]
        maze_exit = self._cells[self._num_cols - 1][self._num_rows - 1]

        maze_entrance.has_left_wall = False
        maze_exit.has_right_wall = False

        maze_entrance.draw()
        maze_exit.draw()

    def break_walls(self, col, row):
        self._cells[col][row].visited = True

        while True:
            # format [[col, row, direction]], [col, row, direction]]
            can_visit = []

            # Check we can move left
            if col >= 1:
                if not self._cells[col - 1][row].visited:
                    # TODO: Move the left, right, up, down to an Enum
                    can_visit.append([col - 1, row, Direction.LEFT])

            # Check we can move right
            if col < self._num_cols - 1:
                if not self._cells[col + 1][row].visited:
                    can_visit.append([col + 1, row, Direction.RIGHT])

            # Check we can move up
            if row >= 1:
                if not self._cells[col][row - 1].visited:
                    can_visit.append([col, row - 1, Direction.UP])

            # Check if we can move down
            if row < self._num_rows - 1:
                if not self._cells[col][row + 1].visited:
                    can_visit.append([col, row + 1, Direction.DOWN])

            if len(can_visit) == 0:
                self._cells[col][row].draw()
                break

            next_cell_move = random.randint(0, len(can_visit) - 1)
            next_cell_values = can_visit[next_cell_move]
            next_cell = self._cells[next_cell_values[0]][next_cell_values[1]]

            match next_cell_values[2]:
                # TODO: Base case from Enum
                case Direction.RIGHT:
                    self._cells[col][row].has_right_wall = False
                    next_cell.has_left_wall = False

                case Direction.LEFT:
                    self._cells[col][row].has_left_wall = False
                    next_cell.has_right_wall = False

                case Direction.UP:
                    self._cells[col][row].has_top_wall = False
                    next_cell.has_bottom_wall = False

                case Direction.DOWN:
                    self._cells[col][row].has_bottom_wall = False
                    next_cell.has_top_wall = False

            self._cells[col][row].draw()
            next_cell.draw()
            self.break_walls(next_cell_values[0], next_cell_values[1])

    def reset_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        solved = self.solve_r(0, 0)
        return solved

    def solve_r(self, col, row):
        self.animate()

        current_cell = self._cells[col][row]
        current_cell.visited = True

        # check if we are at the end of the maze if we are return
        if current_cell == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True

        # Draw our move to each direction
        if col >= 1 and not current_cell.has_left_wall:
            if not self._cells[col - 1][row].visited:
                current_cell.draw_move(self._cells[col - 1][row])
                solved = self.solve_r(col - 1, row)
                if solved:
                    return True
                else:
                    current_cell.draw_move(
                        self._cells[col - 1][row],
                        undo=True
                    )

        if col < self._num_cols - 1 and not current_cell.has_right_wall:
            if not self._cells[col + 1][row].visited:
                current_cell.draw_move(self._cells[col + 1][row])
                solved = self.solve_r(col + 1, row)
                if solved:
                    return True
                else:
                    current_cell.draw_move(
                        self._cells[col + 1][row],
                        undo=True
                    )

        if row >= 1 and not current_cell.has_top_wall:
            if not self._cells[col][row - 1].visited:
                current_cell.draw_move(self._cells[col][row - 1])
                solved = self.solve_r(col, row - 1)
                if solved:
                    return True
                else:
                    current_cell.draw_move(
                        self._cells[col][row - 1],
                        undo=True
                    )

        if row < self._num_rows - 1 and not current_cell.has_bottom_wall:
            if not self._cells[col][row + 1].visited:
                current_cell.draw_move(self._cells[col][row + 1])
                solved = self.solve_r(col, row + 1)
                if solved:
                    return True
                else:
                    current_cell.draw_move(
                        self._cells[col][row + 1],
                        undo=True
                    )

        return False

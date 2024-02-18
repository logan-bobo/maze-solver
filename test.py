from maze import Maze

import unittest


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_and_exit(self):
        m1 = Maze(0, 0, 10, 10, 10, 10, None)

        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )

        self.assertEqual(
            m1._cells[9][9].has_right_wall,
            False
        )

    def test_visit_reset_post_draw(self):
        m1 = Maze(0, 0, 10, 10, 10, 10, None)

        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()

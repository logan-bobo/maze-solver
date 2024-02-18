#!/usr/bin/env python3

import random
from window import Window
from maze import Maze


if __name__ == "__main__":
    window = Window(805, 805)
    maze = Maze(5, 5, 10, 10, 80, 80, window, random.randint(0, 1000))
    window.wait_for_close()

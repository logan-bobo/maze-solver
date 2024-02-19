#!/usr/bin/env python3

import random
from window import Window
from maze import Maze


if __name__ == "__main__":
    window = Window(805, 805)
    maze = Maze(5, 5, 20, 20, 40, 40, window, random.randint(0, 1000))
    window.wait_for_close()

#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int):
        self.root = Tk()
        self.root.title: str = "Maze Solver"
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running: bool = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        # horizontal
        self.x: int = x
        # vertical
        self.y: int = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=2 
        )

        canvas.pack()

class Cell:
    def __init__(
            self, x1, x2, y1, y2, window 
        ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    
    def draw(self):
        if self.has_top_wall:
            top_wall_p1 = Point(self._x1, self._y1)
            top_wall_p2 = Point(self._x2, self._y1)
            top_line = Line(top_wall_p1, top_wall_p2)
            window.draw_line(top_line, "white")
        
        if self.has_right_wall:
            right_wall_p1 = Point(self._x2, self._y1)
            right_wall_p2 = Point(self._x2, self._y2)
            right_line = Line(right_wall_p1, right_wall_p2)
            window.draw_line(right_line, "white")
        
        if self.has_left_wall:
            left_wall_p1 = Point(self._x1, self._y1)
            left_wall_p2 = Point(self._x1, self._y2)
            left_line = Line(left_wall_p1, left_wall_p2)
            window.draw_line(left_line, "white")

        if self.has_bottom_wall:
            bottom_wall_p1 = Point(self._x1, self._y2) 
            bottom_wall_p2 = Point(self._x2, self._y2)
            bottom_line = Line(bottom_wall_p1, bottom_wall_p2)
            window.draw_line(bottom_line, "white")



if __name__ == "__main__":
    window = Window(800, 600)

    # test some line draws
    #p1 = Point(100, 200)
    #p2 = Point(400, 200)

    #l1 = Line(p1, p2)
    
    #window.draw_line(l1, "white")
    
    cell_a = Cell(200, 400, 200, 400, window)
    cell_a.draw()

    window.wait_for_close()



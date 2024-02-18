from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.root = Tk()
        self.root.title: str = "Maze Solver"
        self.canvas = Canvas(height=height, width=width, bg="black")
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
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=2
        )

        canvas.pack()


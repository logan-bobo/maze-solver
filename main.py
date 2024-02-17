#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False        

if __name__ == "__main__":
    window = Window(800, 600)
    window.wait_for_close()

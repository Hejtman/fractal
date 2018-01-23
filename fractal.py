#!/usr/bin/env python3

import random
import tkinter
import numpy as np
from tkinter import ttk


class Fractal:
    def __init__(self, width, height, xa, xb, ya, yb):
        self.width = width
        self.height = height
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb

        self.image = tkinter.PhotoImage(width=width, height=height)
        self.iteration = 0
        self.r = 4
        self.g = 8
        self.b = 16


class Mandelbrot(Fractal):
    def __init__(self, width, height, xa, xb, ya, yb):
        super().__init__(width, height, xa, xb, ya, yb)
        self.data = np.zeros((width, height), dtype=np.complex_)

    def compute(self):
        for y in range(self.height):
            for x in range(self.width):
                c = complex(self.xa + (self.xb - self.xa) * x / self.width,
                            self.ya + (self.yb - self.ya) * y / self.height)
                self.data[x, y] = self.data[x, y]**2 + c

                if abs(self.data[x, y]) < 2.0:
                    rd = hex(self.iteration % self.r * 64)[2:].zfill(2)
                    gr = hex(self.iteration % self.g * 32)[2:].zfill(2)
                    bl = hex(self.iteration % self.b * 16)[2:].zfill(2)
                    self.image.put("#" + rd + gr + bl, (x, y))

        self.iteration += 1
        print(self.iteration)


if __name__ == "__main__":
    WIDTH = 1024
    HEIGHT = 768
    ITERATIONS = 25
    root = tkinter.Tk()

    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    fractal = Mandelbrot(WIDTH, HEIGHT, -2.0, 2.0, -1.5, 1.5)
    fractal.compute()
    canvas.create_image((WIDTH / 2, HEIGHT / 2), image=fractal.image)

    root.mainloop()

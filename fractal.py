#!/usr/bin/env python3

import random
import tkinter
import numpy as np
from tkinter import ttk


class Frame:
    def __init__(self, width, height, fractal):
        self.fractal = fractal

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.root.after("idle", self.compute_and_draw)

    def compute_and_draw(self):
        self.fractal.compute()
        self.canvas.create_image((self.fractal.width / 2,
                                  self.fractal.height / 2), image=self.fractal.image)
        self.root.after(1000, self.compute_and_draw)


class Fractal:
    def __init__(self, width, height, xa, ya, xb, yb):
        self.width = width
        self.height = height
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb

        self.image = None
        self.iteration = 0
        self.r = 4
        self.g = 8
        self.b = 16

    def compute(self):
        if not self.image:
            self.image = tkinter.PhotoImage(width=self.width, height=self.height)


class Mandelbrot(Fractal):
    def __init__(self, width, height, xa, ya, xb, yb):
        super().__init__(width, height, xa, ya, xb, yb)
        self.data = np.zeros((width, height), dtype=np.complex_)

    def compute(self):
        super().compute()
        for y in range(self.height):
            for x in range(self.width):
                z = self.data[x, y]
                if abs(z) >= 2.0:
                    continue

                c = complex(self.xa + (self.xb - self.xa) * x / self.width,
                            self.ya + (self.yb - self.ya) * y / self.height)
                self.data[x, y] = z = z**2 + c

                if abs(z) >= 2.0:
                    rd = hex(self.iteration % self.r * 64)[2:].zfill(2)
                    gr = hex(self.iteration % self.g * 32)[2:].zfill(2)
                    bl = hex(self.iteration % self.b * 16)[2:].zfill(2)
                    self.image.put("#" + rd + gr + bl, (x, y))

        self.iteration += 1
        print(self.iteration)


if __name__ == "__main__":
    world = Frame(width=1024, height=768, fractal=Mandelbrot(1024, 768, -2.0, -1.5, 2.0, 1.5))
    world.root.mainloop()

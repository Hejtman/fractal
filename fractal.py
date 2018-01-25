#!/usr/bin/env python3

import random
import tkinter
import numpy as np
from tkinter import ttk


class Frame:
    def __init__(self, width, height, fractal):
        self.fractal = fractal

        self.image = 0
        self.image_rate = 50
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.root.after("idle", self.compute_and_draw)

    def compute_and_draw(self):
        self.fractal.compute()
        self.canvas.create_image((self.fractal.width / 2,
                                  self.fractal.height / 2), image=self.fractal.images[-1])
        if self.fractal.iteration < self.fractal.iterations:
            self.root.after(self.image_rate, self.compute_and_draw)
        else:
            self.root.after(self.image_rate, self.draw)

    def draw(self):
        print('draw')
        self.canvas.create_image((self.fractal.width / 2,
                                  self.fractal.height / 2), image=self.fractal.images[self.image])
        self.image += 1
        if self.image >= len(self.fractal.images):
            self.image = 0
        self.root.after(self.image_rate, self.draw)


class Fractal:
    def __init__(self, width, height, xa, ya, xb, yb, r, g, b, iterations):
        self.width = width
        self.height = height
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.r = r
        self.g = g
        self.b = b
        self.iterations = iterations

        self.images = []
        self.iteration = 0


class Mandelbrot(Fractal):
    def __init__(self, width, height, xa=-2.0, ya=-1.5, xb=1.0, yb=1.5, r=4, g=8, b=16, iterations=100):
        super().__init__(width, height, xa, ya, xb, yb, r, g, b, iterations)
        self.data = np.zeros((width, height), dtype=np.complex_)

    def compute(self):
        image = tkinter.PhotoImage(width=self.width, height=self.height)
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
                    image.put("#" + rd + gr + bl, (x, y))
                else:
                    i = int(64*(z + 2.0))
                    rd = hex(1*i % 256)[2:].zfill(2)
                    gr = hex(2*i % 256)[2:].zfill(2)
                    bl = hex(4*i % 256)[2:].zfill(2)
                    image.put("#" + rd + gr + bl, (x, y))

        self.images.append(image)
        self.iteration += 1
        print(self.iteration)


if __name__ == "__main__":
    world = Frame(width=1024, height=768, fractal=Mandelbrot(1024, 768, iterations=256))
    world.root.mainloop()

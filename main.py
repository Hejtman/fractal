#!/usr/bin/env python3

import tkinter

from fractal.mandelbrot import Mandelbrot


class Frame:
    def __init__(self, width, height, fractal):
        self.fractal = fractal

        self.image = 0
        self.image_rate = 100
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.root.after("idle", self.action)

    def action(self):
        if self.fractal.iteration < self.fractal.iterations:
            self.fractal.compute()

        self.canvas.create_image((self.fractal.width / 2,
                                  self.fractal.height / 2), image=self.fractal.images[self.image])
        self.image += 1
        if self.image >= len(self.fractal.images):
            self.image = 0

        self.root.after(self.image_rate, self.action)


if __name__ == "__main__":
    world = Frame(width=640, height=480, fractal=Mandelbrot(640, 480, iterations=25))
    world.root.mainloop()

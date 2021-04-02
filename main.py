#!/usr/bin/env python3

import time
import tkinter

from fractal.mandelbrot import Mandelbrot


class Frame:
    def __init__(self, width, height, fractal):
        self.fractal = fractal

        self.image = None
        self.image_shown = 0
        self.image_rate = 100
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.root.after("idle", self.action)

    def colorize(self, iteration):
        if not self.image:
            self.image = tkinter.PhotoImage(width=self.fractal.width, height=self.fractal.height)

        for y in range(self.fractal.height):
            for x in range(self.fractal.width):
                i = self.fractal.decided[x, y]
                if 0 <= i <= iteration:
                    r = hex(16*i % 256)[2:].zfill(2)
                    g = hex(8*i % 256)[2:].zfill(2)
                    b = hex(4*i % 256)[2:].zfill(2)
                    self.image.put("#" + r + g + b, (x, y))

    def action(self):
        if self.fractal.iteration < self.fractal.iterations:
            start_time = time.time()
            self.fractal.compute3()
            print(f'{self.fractal.iteration} {time.time()-start_time}')

        self.colorize(self.image_shown)
        self.canvas.create_image((self.fractal.width / 2,
                                  self.fractal.height / 2), image=self.image)
        self.image_shown += 1
        if self.image_shown >= len(self.fractal.images):
            self.image_shown = 0

        self.root.after(self.image_rate, self.action)


if __name__ == "__main__":
    world = Frame(width=1024, height=768, fractal=Mandelbrot(400, 400, iterations=5))
    world.root.mainloop()

#!/usr/bin/env python3

import time
import tkinter

from fractal.mandelbrot import Mandelbrot
from PIL import Image, ImageTk
import numpy as np


class Frame:
    def __init__(self, width, height, fractal):
        self.fractal = fractal

        self.image = None
        self.image_shown = 0
        self.image_rate = 100
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, bg="blue", width=width, height=height)
        self.canvas.pack()
        self.root.after(100, self.action)

    def action(self):
        if self.fractal.iteration < self.fractal.iterations:
            start_time = time.time()
            self.fractal.compute()
            compute_time = time.time()

        self.image = ImageTk.PhotoImage(image=Image.fromarray(self.fractal.data))
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)
        print(f'iteration={self.fractal.iteration} compute_time={compute_time-start_time} show_time={time.time()-compute_time}')
        self.root.after(100, self.action)


if __name__ == "__main__":
    world = Frame(width=1280, height=1024, fractal=Mandelbrot(1000, 1000, iterations=500))
    world.root.mainloop()

import tkinter
import numpy as np

from . import Fractal


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

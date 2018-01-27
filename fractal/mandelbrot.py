import numpy as np

from . import Fractal


class Mandelbrot(Fractal):
    def __init__(self, width, height, xa=-2.0, ya=-1.5, xb=1.0, yb=1.5, iterations=100):
        super().__init__(width, height, xa, ya, xb, yb, iterations)
        self.data = np.zeros((width, height, iterations), dtype=np.complex_)

    def compute(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.decided[x, y] < 0:
                    z = self.data[x, y, self.iteration-1] if self.iteration else complex(0, 0)
                    c = complex(self.xa + (self.xb - self.xa) * x / self.width,
                                self.ya + (self.yb - self.ya) * y / self.height)
                    self.data[x, y, self.iteration] = z = z**2 + c
                    if abs(z) >= 2.0:
                        self.decided[x, y] = self.iteration
        self.iteration += 1
        print(self.iteration)

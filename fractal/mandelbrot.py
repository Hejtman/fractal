import numpy as np

from . import Fractal


class Mandelbrot(Fractal):
    """
    https://tomroelandts.com/articles/how-to-compute-the-mandelbrot-set-using-numpy-array-operations
    """
    def __init__(self, width, height, xa=-2.0, ya=-1.5, xb=1.0, yb=1.5, iterations=100):
        super().__init__(width, height, xa, ya, xb, yb, iterations)

    def compute(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.decided[x, y] < 0:
                    z = self.data[x, y, self.computing_iteration-1] if self.computing_iteration else complex(0, 0)
                    c = complex(self.xa + (self.xb - self.xa) * x / self.width,
                                self.ya + (self.yb - self.ya) * y / self.height)
                    self.data[x, y, self.computing_iteration] = z = z**2 + c
                    if abs(z) >= 2.0:
                        self.decided[x, y] = self.computing_iteration
        self.computing_iteration += 1

    def compute2(self):
        self.computing_iteration += 1
        for y in range(self.height):
            for x in range(self.width):
                if not self.decided[x, y]:
                    z = self.data[x, y, self.computing_iteration-1]
                    c = complex(self.xa + (self.xb - self.xa) * x / self.width,
                                self.ya + (self.yb - self.ya) * y / self.height)
                    self.data[x, y, self.computing_iteration] = z = z**2 + c
                    if abs(z) >= 2.0:
                        self.decided[x, y] = self.computing_iteration

    def compute3(self):
        self.data[self.M] = self.data[self.M] * self.data[self.M] + self.c[self.M]
        self.M[np.abs(self.data[self.iteration]) > 2] = False
        self.iteration += 1

        #self.data[self.m] = self.data[self.m] * self.data[self.m] + self.c[self.m]
        #self.m[np.abs(self.z) > 2] = self.computing_iteration

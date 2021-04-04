import numpy as np

from . import Fractal


class Mandelbrot(Fractal):
    """
    https://tomroelandts.com/articles/how-to-compute-the-mandelbrot-set-using-numpy-array-operations
    """
    def __init__(self, width, height, xa=-2.0, ya=-1.5, xb=1.0, yb=1.5, iterations=100):
        super().__init__(width, height, xa, ya, xb, yb, iterations)

    def colorize(self):
        return [16*self.iteration, 8*self.iteration, 4*self.iteration]

    def compute(self):
        color = self.colorize()
        self.matrix[self.M] = self.matrix[self.M] * self.matrix[self.M] + self.c[self.M]
        self.data[np.abs(self.matrix) > 2] = color  # FIXME
        self.M[np.abs(self.matrix) > 2] = False     # FIXME
        self.iteration += 1

        #self.matrix[self.m] = self.matrix[self.m] * self.matrix[self.m] + self.c[self.m]
        #self.m[np.abs(self.z) > 2] = self.computing_iteration

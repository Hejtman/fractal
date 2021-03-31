#from dataclasses import dataclass
import numpy as np


#;@dataclass
class Fractal:
    def __init__(self, width, height, xa, ya, xb, yb, total_iterations):
        self.width = width
        self.height = height
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.total_iterations = total_iterations

        self.computing_iteration = 0
        self.data = np.zeros((width, height, total_iterations+1), dtype=np.complex_)
        self.decided = np.zeros((width, height), dtype=np.int16)
        self.images = []

#        self.data.fill(np.complex_(0, 0))
        self.decided.fill(0)

        self.x = np.linspace(-2, 1, num=self.height).reshape((1, self.height))
        self.y = np.linspace(-1, 1, num=self.width).reshape((self.width, 1))
        self.c = np.tile(self.x, (self.width, 1)) + 1j * np.tile(self.y, (1, self.height))

        self.z = np.zeros((self.width, self.height), dtype=complex)
        self.m = np.full((self.width, self.height), 0, dtype=np.int16)

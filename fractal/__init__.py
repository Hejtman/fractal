import numpy as np


class Fractal:
    def __init__(self, width, height, xa, ya, xb, yb, iterations):
        self.width = width
        self.height = height
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.iterations = iterations

        self.images = []
        self.iteration = 0
        self.decided = np.zeros((width, height), dtype=np.int)
        self.decided.fill(-1)

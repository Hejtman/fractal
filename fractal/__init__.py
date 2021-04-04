from dataclasses import dataclass
import numpy as np


@dataclass
class Fractal:
    width: int
    height: int
    x_begin: np.longdouble
    y_begin: np.longdouble
    x_end: np.longdouble
    y_end: np.longdouble
    iterations: int

    def __post_init__(self):
        self.iteration: int = 0
        self.images: list = []
        self.matrix = np.zeros((self.height, self.width), dtype=np.longcomplex)                   # TODO: add dimension > matrix
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.decided = np.full((self.height, self.width), fill_value=-1, dtype=np.int16)        # FIXME: is IN/OUT?

        self.M = np.full((self.height, self.width), fill_value=True, dtype=np.bool_)            # FIXME: use decided instead
        self.line = np.linspace(self.x_begin, self.x_end, num=self.width).reshape((1, self.width))
        self.column = np.linspace(self.y_begin, self.y_end, num=self.height).reshape((self.height, 1))
        self.c = np.tile(self.line, (self.height, 1)) + 1j * np.tile(self.column, (1, self.width))

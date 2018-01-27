class Fractal:
    def __init__(self, width, height, xa, ya, xb, yb, r, g, b, iterations):
        self.width = width
        self.height = height
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.r = r
        self.g = g
        self.b = b
        self.iterations = iterations

        self.images = []
        self.iteration = 0

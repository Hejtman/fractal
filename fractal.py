#!/usr/bin/env python3

import random
import tkinter
from tkinter import ttk


WIDTH = 1024
HEIGHT = 768
ITERATIONS = 25


root = tkinter.Tk()


img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
xa = -2.0
xb = 2.0
ya = -1.5
yb = 1.5
for ky in range(HEIGHT):
    for kx in range(WIDTH):
        c = complex(xa + (xb - xa) * kx / WIDTH, ya + (yb - ya) * ky / HEIGHT)
        z = complex(0.0, 0.0)
        for i in range(ITERATIONS):
            z = z * z + c
            if abs(z) >= 2.0:
                break
        rd = hex(i % 4 * 64)[2:].zfill(2)
        gr = hex(i % 8 * 32)[2:].zfill(2)
        bl = hex(i % 16 * 16)[2:].zfill(2)
        img.put("#" + rd + gr + bl, (kx, ky))

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.create_image((WIDTH/2, HEIGHT/2), image=img)


root.mainloop()

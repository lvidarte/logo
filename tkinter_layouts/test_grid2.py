"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import random
import turtle
import Tkinter as tk

root = tk.Tk()
canvas = turtle.ScrolledCanvas(root, 300, 200, 1000, 1000)
canvas.grid(row=0, column=0, columnspan=3)

turtle._Screen._root = root
turtle._Screen._canvas = canvas

screen = turtle.Screen()
turtle.TurtleScreen.__init__(screen, screen._canvas)


label0 = tk.Label(root, text="label 0")
label0.grid(row=1, column=0)
label1 = tk.Label(root, text="label 1")
label1.grid(row=1, column=1)
label2 = tk.Label(root, text="label 2")
label2.grid(row=1, column=2)

scale = tk.Scale(root, from_=1, to=100)
scale.grid(row=0, column=3, rowspan=2, sticky=tk.N+tk.S, ipadx=10, ipady=10)

#turtle.fd(100)

turtles = [turtle.Turtle() for _ in xrange(20)]
for t in turtles:
    t.right(random.randint(0, 359))
    t.forward(random.randint(50, 200))

tk.mainloop()

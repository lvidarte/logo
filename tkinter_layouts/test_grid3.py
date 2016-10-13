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


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.do()

    def create_widgets(self):
        self.canvas = turtle.ScrolledCanvas(self, 640, 480, 1280, 960)
        self.canvas.grid(row=0, column=0, columnspan=3)

        turtle._Screen._root = self
        turtle._Screen._canvas = self.canvas

        screen = turtle.Screen()
        turtle.TurtleScreen.__init__(screen, screen._canvas)

        self.button_0 = tk.Button(self, text="label 0")
        self.button_0.grid(row=1, column=0)
        self.button_1 = tk.Label(self, text="label 1")
        self.button_1.grid(row=1, column=1)
        self.button_2 = tk.Label(self, text="label 2")
        self.button_2.grid(row=1, column=2)

        self.scale = tk.Scale(self, from_=1, to=100)
        self.scale.grid(row=0, column=3, rowspan=2, sticky=tk.N+tk.S, ipadx=10, ipady=10)

        self.status = tk.Label(self, text="a status bar")
        self.status.grid(row=2, column=0, columnspan=4)

    def do(self):
        turtles = [turtle.Turtle() for _ in xrange(20)]
        for t in turtles:
            t.right(random.randint(0, 359))
            t.forward(random.randint(50, 200))


if __name__ == '__main__':
    app = Application()
    app.mainloop()

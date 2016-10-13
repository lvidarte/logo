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
        self.grid(sticky=tk.W+tk.E+tk.N+tk.S)
        self.create_widgets()
        self.do()

    def create_widgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.canvas = turtle.ScrolledCanvas(self, 640, 480, 1980, 1600)
        self.canvas.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        turtle._Screen._root = self
        turtle._Screen._canvas = self.canvas

        screen = turtle.Screen()
        turtle.TurtleScreen.__init__(screen, screen._canvas)

        self.sidebar = tk.Frame()
        self.sidebar.grid(row=0, column=1, sticky=tk.N)

        self.button_0 = tk.Button(self.sidebar, text="button 1")
        self.button_0.grid(row=0, column=0)
        self.button_1 = tk.Button(self.sidebar, text="button 2")
        self.button_1.grid(row=1, column=0)
        self.button_2 = tk.Button(self.sidebar, text="button 3")
        self.button_2.grid(row=2, column=0)

        self.status = tk.Label(self, text="a status bar")
        self.status.grid(row=1, column=0, columnspan=2)

    def do(self):
        turtles = [turtle.Turtle() for _ in xrange(20)]
        for t in turtles:
            t.right(random.randint(0, 359))
            t.forward(random.randint(50, 200))


if __name__ == '__main__':
    app = Application()
    app.mainloop()

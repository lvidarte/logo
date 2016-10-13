"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle
from Tkinter import Button
from itertools import cycle


def cuadrado(lado):
    for _ in range(4):
        turtle.fd(lado)
        turtle.right(90)

def dibujar(event):
    values = cycle([100, 50])
    for i in range(24):
        cuadrado(values.next())
        turtle.right(15)


if __name__ == '__main__':

    turtle.setup(500, 500)
    turtle.title('Figuras 2')
    turtle.speed(0)

    screen = turtle.Screen()

    boton = Button(screen._root, text="Empezar")
    boton.bind('<Button-1>', dibujar)
    boton.pack()

    turtle.mainloop()

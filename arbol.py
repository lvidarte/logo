"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import turtle

def dibujar_arbol(deep=6, dist=24):
    d = dist * deep
    turtle.left(60)
    turtle.fd(d)
    if deep:
        dibujar_arbol(deep-1, dist-(dist/deep))
    turtle.bk(d)
    turtle.right(120)
    turtle.fd(d)
    if deep:
        dibujar_arbol(deep-1, dist-(dist/deep))
    turtle.bk(d)
    turtle.left(60)


if __name__ == '__main__':

    turtle.setup(700, 500)

    screen = turtle.Screen()
    screen.bgcolor("cyan")
    screen.title('Arbol')

    turtle.speed(0)
    turtle.color('brown')
    turtle.pensize(3)

    turtle.left(90)
    turtle.penup()
    turtle.bk(200)
    turtle.pendown()
    turtle.fd(144)
    dibujar_arbol(6, 24)
    turtle.bk(144)

    turtle.mainloop()

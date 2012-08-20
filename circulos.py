import random
import turtle
from colores import colores

random.shuffle(colores)


WIDTH = 800
HEIGHT = 600


def dibujar_circulo(event):
    radio = random.randint(10, 100)

    turtle.penup()
    turtle.setpos(-WIDTH/2 + event.x, HEIGHT/2 - event.y)
    turtle.right(90)
    turtle.fd(radio)
    turtle.left(90)
    turtle.pendown()

    turtle.color(colores.pop())
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()


if __name__ == '__main__':

    turtle.setup(WIDTH, HEIGHT)
    turtle.title('Circulos')
    turtle.speed(0)
    turtle.hideturtle()

    screen = turtle.Screen()
    screen._root.bind('<Button-1>', dibujar_circulo)

    turtle.mainloop()

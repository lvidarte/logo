import turtle

turtle.speed(0)

def poligono(lados, lado):
    for i in xrange(lados):
        turtle.fd(lado)
        turtle.right(360.0 / lados)


for i in xrange(10):
    poligono(5, 100)
    turtle.right(36)

turtle.mainloop()

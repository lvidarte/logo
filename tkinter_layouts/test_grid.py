import random
import turtle
import Tkinter as tk

root = tk.Tk()
canvas = turtle.ScrolledCanvas(root, 300, 200, 1000, 1000)
canvas.grid()

turtle._Screen._root = root
turtle._Screen._canvas = canvas

screen = turtle.Screen()
turtle.TurtleScreen.__init__(screen, screen._canvas)

#turtle.fd(100)

turtles = [turtle.Turtle() for _ in xrange(20)]
for t in turtles:
    t.right(random.randint(0, 359))
    t.forward(random.randint(50, 200))

tk.mainloop()

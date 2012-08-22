import random
import turtle
import Tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.W+tk.E+tk.N+tk.S)
        self.create_widgets()

    def create_widgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.canvas = turtle.ScrolledCanvas(self, 960, 540, 1920, 1080)
        self.canvas.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        turtle._Screen._root = self
        turtle._Screen._canvas = self.canvas

        self.screen = turtle.Screen()
        turtle.TurtleScreen.__init__(self.screen, self.screen._canvas)

        self.sidebar = tk.Frame()
        self.sidebar.grid(row=0, column=1, sticky=tk.N)

        self.button_1 = tk.Button(self.sidebar, text="Tortugas 1",
                                  command=self.example_1)
        self.button_1.grid(row=0, column=0)
        self.button_2 = tk.Button(self.sidebar, text="Tortugas 2",
                                  command=self.example_2)
        self.button_2.grid(row=1, column=0)
        self.button_3 = tk.Button(self.sidebar, text="Circulos",
                                  command=self.example_3)
        self.button_3.grid(row=2, column=0)

        self.scl_speed = tk.Scale(self.sidebar, from_=1, to=11,
                               label='Velocidad', orient=tk.HORIZONTAL)
        self.scl_speed.grid(row=3, column=0)
        self.scl_speed.set(6)

        #self.status = tk.Label(self, text="a status bar")
        #self.status.grid(row=1, column=0, columnspan=2)

    def clear(self):
        self.screen.clear()
        turtle.speed(self.scl_speed.get())

    def example_1(self):
        self.clear()
        turtles = [turtle.Turtle() for _ in xrange(5)]
        for t in turtles:
            t.speed(self.scl_speed.get())
            t.right(random.randint(0, 359))
            t.forward(random.randint(50, 200))

    def example_2(self):
        self.clear()
        turtles = [turtle.Turtle() for _ in xrange(5)]
        def square(turtle):
            side = random.randint(10, 100)
            for i in xrange(4):
                turtle.fd(side)
                turtle.right(90)
        for t in turtles:
            t.speed(self.scl_speed.get())
            t.penup()
            t.setpos([random.randint(-200, 200) for x in (1,2)])
            t.pendown()
            square(t)

    def example_3(self):
        self.clear()
        n = random.randint(3, 12)
        for i in range(n):
            turtle.circle(n * 5)
            turtle.right(360.0 / n)


if __name__ == '__main__':
    app = Application()
    app.mainloop()

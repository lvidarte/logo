import turtle
import Tkinter as tk


def estrella(lados, largo, angulo):
    for i in range(lados):
        turtle.left(angulo)
        turtle.forward(largo)
        turtle.right((360.0 / lados) + angulo)
        turtle.forward(largo)


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

        self.lados = tk.Scale(self.sidebar, from_=5, to=50,
                              label='lados', orient=tk.HORIZONTAL)
        self.lados.grid(row=0, column=0)
        self.lados.set(15)

        self.largo = tk.Scale(self.sidebar, from_=5, to=200,
                              label='largo', orient=tk.HORIZONTAL)
        self.largo.grid(row=1, column=0)
        self.largo.set(100)

        self.angulo = tk.Scale(self.sidebar, from_=0, to=180,
                               label='angulo', orient=tk.HORIZONTAL)
        self.angulo.grid(row=2, column=0)
        self.angulo.set(140)

        self.begin = tk.Button(self.sidebar, text="Empezar")
        self.begin.grid(row=3, column=0)
        self.begin.bind('<Button-1>', self.draw)

        self.reset = tk.Button(self.sidebar, text="erase")
        self.reset.grid(row=4, column=0)
        self.reset.bind('<Button-1>', self.erase)

    def draw(self, event):
        estrella(self.lados.get(), self.largo.get(), self.angulo.get())

    def erase(self, event):
        turtle.reset()
        turtle.speed(10) # Fast


if __name__ == '__main__':
    app = Application()
    app.mainloop()


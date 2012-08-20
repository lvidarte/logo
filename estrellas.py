import turtle
import Tkinter as tk


def estrella(lados, largo, angulo):
    for i in range(lados):
        turtle.left(angulo)
        turtle.forward(largo)
        turtle.right((360.0 / lados) + angulo)
        turtle.forward(largo)

if __name__ == '__main__':

    turtle.setup(600, 800)

    screen = turtle.Screen()
    screen.title('Estrellas')

    lados = tk.Scale(screen._root, from_=5, to=50,
                     label='lados', orient=tk.HORIZONTAL)
    largo = tk.Scale(screen._root, from_=5, to=200,
                    label='largo', orient=tk.HORIZONTAL)
    angulo = tk.Scale(screen._root, from_=0, to=180,
                      label='angulo', orient=tk.HORIZONTAL)

    lados.set(15)
    largo.set(100)
    angulo.set(140)

    def dibujar(event):
        estrella(lados.get(), largo.get(), angulo.get())

    boton = tk.Button(screen._root, text="Empezar")
    boton.bind('<Button-1>', dibujar)

    def borrar(event):
        turtle.reset()
        turtle.speed(10) # Fast

    reset = tk.Button(screen._root, text="Borrar")
    reset.bind('<Button-1>', borrar)

    lados.pack(side=tk.LEFT)
    largo.pack(side=tk.LEFT)
    angulo.pack(side=tk.LEFT)
    boton.pack(side=tk.LEFT)
    reset.pack(side=tk.LEFT)

    borrar(None)
    turtle.mainloop()





from tkinter import ttk
from tkinter import *

class vista:
    def __init__(self, window):
        self.win = window
        self.win.title('products aplication')

        #creando un contenedoor de frame
        frame = LabelFrame(self.win, text = 'Registra un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #name input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #price input
        Label(frame, text = 'precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        #boton agregar producto
        ttk.Button(frame, text = 'guardar producto').grid(row = 3, columnspan = 4, sticky = W + E)

        #se crea la tabla donde se van a mostrar los productos
        self.tree = ttk.Treeview(height = 15, columns = 4)
        self.tree.grid(row = 4, column = 0, columnspan = 2)

if __name__ == '__main__':
    window = Tk()
    aplication = vista(window)
    window.mainloop()

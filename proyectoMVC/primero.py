from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = 'database.db'

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
        ttk.Button(frame, text = 'guardar producto').grid(row = 3, columnspan = 2, sticky = W + E)

        #tabla
        self.tree = ttk.Treeview(height = 10, columns = 4)
        self.tree.grid(row = 4, column = 0, columnspan = 1)
        self.tree.heading('#0', text = 'nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'price', anchor = CENTER)

        self.get_products()

    def run_query(self, query, parameters = ()):
        #se crea la conexion
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        #se obtienen los datos de la tabla
        records = self.tree.get_children()

        #limpiando la tabla
        query = 'SELECT * FROM productos ORDER BY name DESC'
        bd_rows = self.run_query(query)

        print(bd_rows)






if __name__ == '__main__':
    window = Tk()
    aplication = Product(window)
    window.mainloop()

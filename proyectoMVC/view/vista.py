from controller.controller import interacciones
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
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        #price input
        Label(frame, text = 'precio: ').grid(row = 2, column = 0)
        self.precio = Entry(frame)
        self.precio.grid(row = 2, column = 1)

        #cantidad input
        Label(frame, text = 'Cantidad: ').grid(row = 3, column = 0)
        self.cantidad = Entry(frame)
        self.cantidad.focus()
        self.cantidad.grid(row = 3, column = 1)

        #boton agregar producto
        ttk.Button(frame, text = 'guardar producto', command = self.add_producto).grid(row = 4, columnspan = 2, sticky = W + E)

        #mensajes
        self.mensaje = Label(text = '', fg = 'red')
        self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        #se crea la tabla donde se van a mostrar los productos
        self.tree = ttk.Treeview(height = 10, columns = ("1", "2"))
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'precio', anchor = CENTER)
        self.tree.heading('#2', text = 'cantidad', anchor = CENTER)
        #botones de eliminar y editar
        ttk.Button(text = 'Borrar', command = self.eliminar_producto).grid(row = 6, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar', command = self.editar_producto).grid(row = 6, column = 1, sticky = W + E)


        #llenando las filas de la tabla
        self.mostrar_productos()

    def mostrar_productos(self):
        records = self.tree.get_children()
        for elemento in records:
            self.tree.delete(elemento)

        enlace = interacciones()
        enlace.get_producto()

        for fila in enlace.bd_filas:
            self.tree.insert('', 0, text = fila[1], values = (fila[2], fila[3]))

    def validacion(self):
        return len(self.nombre.get()) != 0 and len(self.precio.get()) != 0 and len(self.cantidad.get()) != 0

    def add_producto(self):
        enlace = interacciones()
        if self.validacion():
            enlace.set_producto(self.nombre.get(), self.precio.get(), self.cantidad.get())
            self.mensaje['text'] = 'Producto {} agregado correctamente'.format(self.nombre.get())
            self.nombre.delete(0, END)
            self.precio.delete(0, END)
            self.cantidad.delete(0, END)
        else:
            self.mensaje['text'] = 'Todos los campos son requeridos'
        self.mostrar_productos()

    def eliminar_producto(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'No se a seleccionado nada'
            return
        self.mensaje['text'] = ''
        enlace = interacciones()
        nombre = self.tree.item(self.tree.selection())['text']
        enlace.delete_producto(nombre)
        self.mensaje['text'] = 'producto eliminado correctamente'
        self.mostrar_productos()

    def editar_producto(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'No se a seleccionado nada'
            return
        nombre = self.tree.item(self.tree.selection())['text']
        #antiguo_precio = self.tree.item(self.tree.selection())['values'][0]
        antigua_cantidad = self.tree.item(self.tree.selection())['values'][1]
        self.editar_ventana = Toplevel()
        self.editar_ventana.title = 'EDITAR PRODUCTO'

        #nombre antiguo

        Label(self.editar_ventana, text = 'producto a editar:').grid(row = 0, column = 1)
        Entry(self.editar_ventana, textvariable = StringVar(self.editar_ventana, value=nombre), state = 'readonly').grid(row = 0, column = 2)

        #nuevo nombre
        #Label(self.editar_ventana, text = 'nuevo nombre: ').grid(row = 1, column = 1)
        #nuevo_nombre = Entry(self.editar_ventana)
        #nuevo_nombre.grid(row = 1, column = 2)

        #antiguo precio
        #Label(self.editar_ventana, text = 'antiguo precio: ').grid(row = 2, column = 1)
        #Entry(self.editar_ventana, textvariable = StringVar(self.editar_ventana, value = antiguo_precio), state = 'readonly').grid(row = 2, column = 2)

        #nuevo precio
        #Label(self.editar_ventana, text = 'nuevo precio: ').grid(row = 3, column = 1)
        #nuevo_precio = Entry(self.editar_ventana)
        #nuevo_precio.grid(row = 3, column = 2)

        #antiguo cantidad
        Label(self.editar_ventana, text = 'antigua cantidad: ').grid(row = 1, column = 1)
        Entry(self.editar_ventana, textvariable = StringVar(self.editar_ventana, value = antigua_cantidad), state = 'readonly').grid(row = 1, column = 2)

        #nueva cantidad
        Label(self.editar_ventana, text = 'nueva cantidad: ').grid(row = 2, column = 1)
        nueva_cantidad = Entry(self.editar_ventana)
        nueva_cantidad.grid(row = 2, column = 2)

        #creamos un botan para actualizar los datos
        Button(self.editar_ventana, text = 'ACTUALIZAR', command = lambda: self.edit_products(nueva_cantidad.get(), antigua_cantidad)).grid(row=5, column = 2, sticky = W)

    def edit_products(self, nueva_cantidad, antigua_cantidad):
        enlace = interacciones()
        enlace.editar_registro(nueva_cantidad, antigua_cantidad)
        self.editar_ventana.destroy()
        self.mensaje['text'] = 'producto actualizado'
        self.mostrar_productos()









if __name__ == '__main__':
    window = Tk()
    aplication = vista(window)
    window.mainloop()



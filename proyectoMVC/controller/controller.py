from model.conexion_bd import conexion

#se hace la consulta a la base de datos

class interacciones:
    def __init__(self):
        pass

    def get_producto(self):

        #se especifica lo que se quiere hacer
        query = 'SELECT * FROM productos ORDER BY name DESC'
        enlace = conexion()
        self.bd_filas = enlace.ejecuta_consulta(query)

    def set_producto(self, nombre, precio, cantidad):
        query = 'INSERT INTO productos VALUES(NULL, ?, ?, ?)'
        parametros = (nombre, precio, cantidad)
        enlace = conexion()
        enlace.ejecuta_consulta(query, parametros)

    def delete_producto(self, nombre):
        query = 'DELETE FROM productos WHERE name = ?'
        enlace = conexion()
        enlace.ejecuta_consulta(query, (nombre, ))

    def editar_registro(self, nueva_cantidad, antigua_cantidad):
        query = 'UPDATE productos SET cantidad = ? WHERE cantidad = ?'
        parametros = (nueva_cantidad, antigua_cantidad)
        enlace = conexion()
        enlace.ejecuta_consulta(query, parametros)





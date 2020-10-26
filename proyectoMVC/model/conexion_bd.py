import sqlite3


class conexion:
    db_nombre = 'database.db'
    def __init__(self):
        pass

    # nos conectamos a la base de datos
    def ejecuta_consulta(self, query, parameters=()):

        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parameters)
            conn.commit()
        return resultado

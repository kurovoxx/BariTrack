from DataBase import DataBase
import sqlite3

class GraficoRepositorio:
    def __init__(self, db: DataBase) -> None:
        self.db = db

    def get_datos(self, tabla: str, where: str) -> list:
        """
        Obtiene datos de la tabla especificada que cumplen con la condición 'where'.
        """
        try:
            query = f"SELECT * FROM {tabla} WHERE {where}"
            self.db.cursor.execute(query)
            datos = self.db.cursor.fetchall()
            return datos
        except sqlite3.Error as e:
            print(f"Error al obtener los datos: {e}")
            return []

    def update_datos(self, tabla: str, where: str, new_dato: dict) -> bool:
        """
        Actualiza los datos en la tabla especificada, según la condición 'where'.
        Los nuevos datos deben ser pasados como un diccionario {'columna': valor}.
        """
        try:
            set_clause = ", ".join([f"{col} = ?" for col in new_dato.keys()])
            values = list(new_dato.values())
            query = f"UPDATE {tabla} SET {set_clause} WHERE {where}"
            self.db.cursor.execute(query, values)
            self.db.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error al actualizar los datos: {e}")
            return False

from DataBase import DataBase
from InterfaceAdapter import Adapter


class AdapterDb(Adapter):
    def __init__(self, route):
        self.db = DataBase(route)
        self.db.conectar()

    def obtener_valor(self, query, params=()):
        """Ejecuta una consulta y devuelve el primer valor del primer registro."""
        self.db.cursor.execute(query, params)
        resultado = self.db.cursor.fetchone()
        return resultado[0] if resultado else None

    def obtener_lista(self, query, params=()):
        """Ejecuta una consulta y devuelve una lista de todos los registros."""
        self.db.cursor.execute(query, params)
        return self.db.cursor.fetchall()

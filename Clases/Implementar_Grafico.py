from abc import ABC, abstractmethod
import sqlite3

class Implementar_Grafico(ABC):

    @abstractmethod
    def obtener_datos(self):
        pass

    @abstractmethod
    def crear_grafico(self, datos, frame):
        pass

    def _ejecutar_consulta(self, usuario, query):
        conexion = sqlite3.connect(f"./users/{usuario}/alimentos.db")
        cursor = conexion.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
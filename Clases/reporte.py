from abc import ABC, abstractmethod
from datetime import datetime

class GeneradorReporte(ABC):
    def __init__(self, usuario, calcular_imc, calcular_TMB, cargar_datos_usuario):
        self.usuario = usuario
        self.calcular_imc = calcular_imc
        self.calcular_TMB = calcular_TMB
        self.cargar_datos_usuario = cargar_datos_usuario
        self.fecha = datetime.now().strftime("%d/%m/%Y")

    def generar(self):
        datos_usuario = self.cargar_datos_usuario()
        imc = self.calcular_imc()
        tmb = self.calcular_TMB()
        historial_peso = self.obtener_historial_peso()
        contenido = self.construir_contenido(datos_usuario, imc, tmb, historial_peso)
        nombre_archivo = self.obtener_nombre_archivo()
        self.guardar_archivo(nombre_archivo, contenido)
        self.mostrar_mensaje(nombre_archivo)

    def obtener_historial_peso(self):
        import sqlite3
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute("SELECT peso, fecha FROM peso ORDER BY fecha DESC LIMIT 5")
            historial = cursor.fetchall()
            conn.close()
            return historial
        except sqlite3.Error:
            return []

    @abstractmethod
    def construir_contenido(self, datos_usuario, imc, tmb, historial):
        pass

    @abstractmethod
    def guardar_archivo(self, nombre_archivo, contenido):
        pass

    @abstractmethod
    def obtener_nombre_archivo(self):
        pass

    @abstractmethod
    def mostrar_mensaje(self, nombre_archivo):
        pass

from customtkinter import *
from CTkMessagebox import CTkMessagebox
from Clases.reporte import GeneradorReporte

class GeneradorTexto(GeneradorReporte):
    def construir_contenido(self, datos, imc, tmb, historial):
        texto = f"Reporte de Salud - {self.usuario}\nFecha: {self.fecha}\n\n"
        texto += f"Edad: {datos[0]}\nGénero: {datos[1]}\nPeso actual: {datos[2]} kg\n"
        texto += f"Estatura: {datos[5]} cm\nNivel de actividad: {datos[3]}\n"
        texto += f"IMC: {imc:.2f}\nTMB: {tmb:.2f} kcal/día\n\nHistórico de peso:\n"
        for peso, fecha in historial:
            texto += f"{fecha} - {peso} kg\n"
        return texto

    def obtener_nombre_archivo(self):
        return f"./users/{self.usuario}/salud_{self.fecha.replace('/', '-')}.txt"

    def guardar_archivo(self, nombre_archivo, contenido):
        with open(nombre_archivo, "w") as f:
            f.write(contenido)

    def mostrar_mensaje(self, nombre_archivo):
        CTkMessagebox(title="Texto generado", message=f"Archivo guardado:\n{nombre_archivo}", icon="check", option_1="OK")

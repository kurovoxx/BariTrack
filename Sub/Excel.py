from openpyxl import Workbook
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from Clases.reporte import GeneradorReporte

class GeneradorExcel(GeneradorReporte):
    def construir_contenido(self, datos, imc, tmb, historial):
        wb = Workbook()
        ws = wb.active
        ws.title = "Salud"
        ws.append(["Nombre", self.usuario])
        ws.append(["Fecha", self.fecha])
        ws.append([])
        ws.append(["Edad", datos[0]])
        ws.append(["Género", datos[1]])
        ws.append(["Peso actual", f"{datos[2]} kg"])
        ws.append(["Estatura", f"{datos[5]} cm"])
        ws.append(["Nivel actividad", datos[3]])
        ws.append(["IMC", imc])
        ws.append(["TMB", tmb])
        ws.append([])
        ws.append(["Fecha", "Peso (kg)"])
        for peso, fecha in historial:
            ws.append([fecha, peso])
        return wb

    def obtener_nombre_archivo(self):
        return f"./users/{self.usuario}/salud_{self.fecha.replace('/', '-')}.xlsx"

    def guardar_archivo(self, nombre_archivo, contenido):
        contenido.save(nombre_archivo)

    def mostrar_mensaje(self, nombre_archivo):
        CTkMessagebox(title="Excel generado", message=f"Archivo guardado:\n{nombre_archivo}", icon="check", option_1="OK")

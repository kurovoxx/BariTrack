from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from Clases.reporte import GeneradorReporte

class GeneradorPDF(GeneradorReporte):
    def construir_contenido(self, datos, imc, tmb, historial):
        return (datos, imc, tmb, historial)

    def obtener_nombre_archivo(self):
        return f"./users/{self.usuario}/salud_{self.fecha.replace('/', '-')}.pdf"

    def guardar_archivo(self, nombre_archivo, contenido):
        datos, imc, tmb, historial = contenido
        edad, genero, peso, nivel_actividad, meta_cal, estatura = datos

        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        ancho, alto = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, alto - 50, f"Reporte de Salud - {self.usuario}")
        c.setFont("Helvetica", 12)
        c.drawString(50, alto - 80, f"Fecha: {self.fecha}")

        # Información del usuario
        y = alto - 120
        c.drawString(50, y, f"Edad: {edad}")
        c.drawString(200, y, f"Género: {genero}")
        y -= 20
        c.drawString(50, y, f"Estatura: {estatura} cm")
        c.drawString(200, y, f"Peso actual: {peso} kg")
        y -= 20
        c.drawString(50, y, f"Nivel de actividad: {nivel_actividad}")
        c.drawString(200, y, f"Meta calórica: {meta_cal} kcal")
        y -= 20
        c.drawString(50, y, f"IMC: {round(imc, 2)}")
        c.drawString(200, y, f"TMB: {round(tmb, 2)} kcal")

        # Historial de peso
        y -= 40
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Historial de peso")
        c.setFont("Helvetica", 12)
        y -= 20

        for peso, fecha_peso in historial:
            c.drawString(70, y, str(fecha_peso))
            c.drawString(170, y, f"{peso} kg")
            y -= 20
            if y < 50: 
                c.showPage()
                y = alto - 50

        c.save()


    def mostrar_mensaje(self, nombre_archivo):
        CTkMessagebox(title="PDF generado", message=f"Archivo guardado:\n{nombre_archivo}", icon="check", option_1="OK")

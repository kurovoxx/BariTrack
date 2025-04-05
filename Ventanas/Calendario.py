import customtkinter as ctk
from Ventanas.Ventana_interfaz import New_ventana
from tkinter import messagebox
from tkcalendar import Calendar
import sqlite3
from util.colores import *
from CTkMessagebox import CTkMessagebox
from datetime import datetime


class Calendario(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color, 'calendario')
        self.panel_principal = panel_principal
        self.add_widget_calendario()
        self.mensage(
            "Selecciona una fecha para agregarla a la base de datos.", "Calendario")
        self.cargar_fechas_resaltadas()  # Cargar las fechas al iniciar

    def add_widget_calendario(self):
        # Crear calendario
        self.calendario = Calendar(
            self.panel_principal, selectmode='day', date_pattern='yyyy-mm-dd', showweeknumbers=False)
        self.calendario.place(relx=0.5, rely=0.4, anchor="center")

        # Botón para guardar la fecha seleccionada
        self.boton_guardar = ctk.CTkButton(self.panel_principal, text="Guardar Fecha",
                                           command=self.guardar_fecha, corner_radius=15, width=200, height=40,
                                           font=("Times New Roman", 15, "italic"), text_color="white")
        self.boton_guardar.place(relx=0.5, rely=0.7, anchor="center")

    def guardar_fecha(self):
        fecha_seleccionada = self.calendario.get_date()
        try:
            # Conectar a la base de datos
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            # Insertar la fecha seleccionada
            cursor.execute(
                "INSERT INTO fechas_seleccionadas (fecha) VALUES (?)", (fecha_seleccionada,))
            conn.commit()

            CTkMessagebox(title="Fecha Guardada",
                          message=f"Fecha {fecha_seleccionada} guardada con éxito.", icon='info', option_1="Ok")

            conn.close()

            # Resaltar la fecha en el calendario
            self.resaltar_fecha(fecha_seleccionada)

        except sqlite3.Error as e:
            print(f"Error al guardar la fecha: {e}")
            CTkMessagebox(
                title="Error", message="Hubo un error al guardar la fecha.", icon='error', option_1="Ok")

    def resaltar_fecha(self, fecha):
        """Resaltar la fecha seleccionada en el calendario."""
        # Convertir la fecha de cadena a objeto datetime
        fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d").date()

        self.calendario.calevent_create(
            fecha_datetime, "Fecha Seleccionada", tags='resaltada')  # Resalta la fecha
        self.calendario.tag_config(
            'resaltada', background='green', foreground='white')

    def cargar_fechas_resaltadas(self):
        """Cargar las fechas desde la base de datos y resaltarlas en el calendario."""
        try:
            # Conectar a la base de datos
            conn = sqlite3.connect(f"./users/{self.usuario}/fechas.db")
            cursor = conn.cursor()

            # Obtener todas las fechas guardadas
            cursor.execute("SELECT fecha FROM fechas_seleccionadas")
            fechas = cursor.fetchall()

            conn.close()

            # Resaltar las fechas obtenidas
            for fecha in fechas:
                self.resaltar_fecha(fecha[0])  # Resaltar cada fecha

        except sqlite3.Error as e:
            print(f"Error al cargar las fechas: {e}")
            CTkMessagebox(
                title="Error", message="Hubo un error al cargar las fechas.", icon='error', option_1="Ok")

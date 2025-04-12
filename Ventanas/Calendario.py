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
            self.panel_principal, selectmode='day', date_pattern='yyyy-mm-dd', showweeknumbers=False, background=azul_medio_oscuro)
        self.calendario.place(relx=0.25, rely=0.32, anchor="center")

        #Lista de recordatorios (scrolleable)

        self.frame_recordatorios= ctk.CTkScrollableFrame(
            self.panel_principal, width=350, height=268, corner_radius=15, fg_color=azul_medio_oscuro
        )
        self.frame_recordatorios.place(relx=0.72, rely=0.32, anchor="center")

        #Boton para editar los recordatorios#

        self.boton_editar = ctk.CTkButton(self.panel_principal, text="Editar Recordatorios",
            corner_radius=15, width=200, height=40, font=("Times New Roman", 15, "italic"), text_color="white"
        )
        self.boton_editar.place(relx=0.72, rely=0.7, anchor="center")

        

        

        # Campo para ingresar la descripción
        self.entrada_descripcion = ctk.CTkEntry(
            self.panel_principal, placeholder_text="Escribe una descripción...", width=250, height=35,
            corner_radius=10, font=("Times New Roman", 14))
        self.entrada_descripcion.place(relx=0.25, rely=0.55, anchor="center")

        # Botón para guardar la fecha seleccionada
        self.boton_guardar = ctk.CTkButton(self.panel_principal, text="Guardar Fecha",
                                        command=self.guardar_fecha, corner_radius=15, width=200, height=40,
                                        font=("Times New Roman", 15, "italic"), text_color="white")
        self.boton_guardar.place(relx=0.25, rely=0.7, anchor="center")

    def guardar_fecha(self):
        fecha_seleccionada = self.calendario.get_date()
        descripcion = self.entrada_descripcion.get()  # Obtener texto de la entrada

        if not descripcion.strip():
            CTkMessagebox(title="Campo vacío", message="Por favor ingresa una descripción.",
                        icon="warning", option_1="Ok")
            return

        try:
            # Conectar a la base de datos
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            # Insertar la fecha y descripción
            cursor.execute(
                "INSERT INTO fechas_seleccionadas (fecha, descripcion) VALUES (?,?)",
                (fecha_seleccionada, descripcion)
            )
            conn.commit()

            CTkMessagebox(title="Fecha Guardada",
                        message=f"Fecha {fecha_seleccionada} guardada con éxito.", icon='info', option_1="Ok")

            conn.close()

            # Resaltar la fecha en el calendario
            self.resaltar_fecha(fecha_seleccionada)

            # Limpiar campo de texto
            self.entrada_descripcion.delete(0, 'end')

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
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
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

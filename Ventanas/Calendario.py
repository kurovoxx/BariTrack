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
        self.recordatorio_seleccionado = None  # Variable para guardar el ID del recordatorio seleccionado
        self.add_widget_calendario()    
        self.mensage(
            "Selecciona una fecha para agregarla a la base de datos.", "Calendario")
        self.cargar_fechas_resaltadas()  # Cargar las fechas al iniciar
        self.cargar_lista_recordatorios()  # Cargar los recordatorios al iniciar

    def add_widget_calendario(self):
        # Crear calendario
        self.calendario = Calendar(
            self.panel_principal, 
            selectmode='day', 
            date_pattern='dd/mm/yyyy',  # Cambiado para que coincida con el formato de tu imagen
            showweeknumbers=False, 
            background=azul_medio_oscuro,
            locale='es_ES'  # Para que esté en español
        )
        self.calendario.place(relx=0.25, rely=0.32, anchor="center")

        # Lista de recordatorios (scrolleable)
        self.frame_recordatorios = ctk.CTkScrollableFrame(
            self.panel_principal, 
            width=350, 
            height=268, 
            corner_radius=15, 
            fg_color=azul_medio_oscuro
        )
        self.frame_recordatorios.place(relx=0.72, rely=0.32, anchor="center")

        "==== Botones ===="

        # Botón para editar los recordatorios
        self.boton_editar = ctk.CTkButton(
            self.panel_principal, 
            text="Editar Recordatorios",
            corner_radius=15, 
            width=200, 
            height=40, 
            font=("Times New Roman", 15, "italic"), 
            text_color="white",
            command=self.editar_recordatorio
        )
        self.boton_editar.place(relx=0.72, rely=0.7, anchor="center")

        # Botón para borrar recordatorios
        self.boton_borrar = ctk.CTkButton(
            self.panel_principal, 
            text="Borrar Recordatorio",
            corner_radius=15, 
            width=200, 
            height=40, 
            font=("Times New Roman", 15, "italic"), 
            text_color="white",
            fg_color="#FF5555",  
            hover_color="#FF3333",
            command=self.borrar_recordatorio
        )
        self.boton_borrar.place(relx=0.72, rely=0.80, anchor="center")

        # Campo para ingresar la descripción
        self.entrada_descripcion = ctk.CTkEntry(
            self.panel_principal, 
            placeholder_text="Escribe una descripción...", 
            width=250, 
            height=35,
            corner_radius=10, 
            font=("Times New Roman", 14)
        )
        self.entrada_descripcion.place(relx=0.25, rely=0.55, anchor="center")

        # Botón para guardar la fecha seleccionada
        self.boton_guardar = ctk.CTkButton(
            self.panel_principal, 
            text="Agregar Fecha",  # Cambiado para que coincida con tu imagen
            command=self.guardar_fecha, 
            corner_radius=15, 
            width=200, 
            height=40,
            font=("Times New Roman", 15, "italic"), 
            text_color="white"
        )
        self.boton_guardar.place(relx=0.25, rely=0.7, anchor="center")

    def guardar_fecha(self):
        fecha_seleccionada = self.calendario.get_date()
        descripcion = self.entrada_descripcion.get().strip()

        if not descripcion:
            CTkMessagebox(
                title="Campo vacío", 
                message="Por favor ingresa una descripción.",
                icon="warning", 
                option_1="Ok"
            )
            return

        try:
            fecha_db = datetime.strptime(fecha_seleccionada, "%d/%m/%Y").strftime("%Y-%m-%d")
            
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()

            if self.recordatorio_seleccionado:
                cursor.execute(
                    "UPDATE fechas_seleccionadas SET fecha=?, descripcion=? WHERE id=?",
                    (fecha_db, descripcion, self.recordatorio_seleccionado)
                )
                mensaje = f"Recordatorio #{self.recordatorio_seleccionado} actualizado."
                self.recordatorio_seleccionado = None
                self.boton_guardar.configure(text="Agregar Fecha")  
            else:
                # Modo agregar nuevo
                cursor.execute(
                    "INSERT INTO fechas_seleccionadas (fecha, descripcion) VALUES (?, ?)",
                    (fecha_db, descripcion)
                )
                mensaje = f"Recordatorio agregado para {fecha_seleccionada}."

            conn.commit()
            conn.close()

            CTkMessagebox(
                title="Éxito",
                message=mensaje,
                icon='info', 
                option_1="Ok"
            )

            self.resaltar_fecha(fecha_db)
            self.entrada_descripcion.delete(0, 'end')
            self.cargar_lista_recordatorios()

        except sqlite3.Error as e:
            print(f"Error al guardar la fecha: {e}")
            CTkMessagebox(
                title="Error", 
                message="Hubo un error al guardar la fecha.", 
                icon='error', 
                option_1="Ok"
            )

    def resaltar_fecha(self, fecha):
        "Resaltar la fecha seleccionada en el calendario."
        try:
            fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d").date()
            self.calendario.calevent_create(
                fecha_datetime, "Fecha Seleccionada", tags='resaltada')
            self.calendario.tag_config(
                'resaltada', background='green', foreground='white')
        except ValueError as e:
            print(f"Error al resaltar fecha: {e}")

    def cargar_fechas_resaltadas(self):
        "Cargar las fechas desde la base de datos y resaltarlas en el calendario."
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute("SELECT fecha FROM fechas_seleccionadas")
            fechas = cursor.fetchall()
            conn.close()

            for fecha in fechas:
                self.resaltar_fecha(fecha[0])

        except sqlite3.Error as e:
            print(f"Error al cargar las fechas: {e}")
            CTkMessagebox(
                title="Error", 
                message="Hubo un error al cargar las fechas.", 
                icon='error', 
                option_1="Ok"
            )
            
    def cargar_lista_recordatorios(self):
    #Limpiar frame
        for widget in self.frame_recordatorios.winfo_children():
            widget.destroy()

        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, fecha, descripcion FROM fechas_seleccionadas ORDER BY fecha")
            filas = cursor.fetchall()
            conn.close()

            for fila in filas:
                recordatorio_id, fecha_db, descripcion = fila
                fecha = datetime.strptime(fecha_db, "%Y-%m-%d").strftime("%d/%m/%Y")
                texto = f"{fecha} {descripcion}"

                btn = ctk.CTkButton(
                    self.frame_recordatorios, 
                    text=texto, 
                    anchor="w",
                    fg_color="#ffffff" if recordatorio_id != self.recordatorio_seleccionado else "#4CAF50",
                    text_color="black",
                    width=350,
                    height=40, 
                    hover_color="#DDDDDD",
                    command=lambda rid=recordatorio_id: self.seleccionar_recordatorio(rid)
                )
                btn.pack(pady=5, padx=5, fill='x')

        except Exception as e:
            print("Error cargando lista:", e)
            CTkMessagebox(
                title="Error", 
                message="Error al cargar los recordatorios.", 
                icon='error', 
                option_1="Ok"
            )
        
    def seleccionar_recordatorio(self, recordatorio_id):
        "Selecciona un recordatorio para editar o borrar"
        if self.recordatorio_seleccionado == recordatorio_id:
            self.recordatorio_seleccionado = None
        else:
            self.recordatorio_seleccionado = recordatorio_id
        
        self.cargar_lista_recordatorios()

    def editar_recordatorio_directo(self, recordatorio_id):
        "Edicion directa del recordatorio seleccionado"
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT descripcion FROM fechas_seleccionadas WHERE id=?",
                (recordatorio_id,)
            )
            descripcion = cursor.fetchone()[0]
            conn.close()

     
            ventana_edicion = ctk.CTkToplevel(self.panel_principal)
            ventana_edicion.title("Editar Recordatorio")
            ventana_edicion.geometry("400x150")
            ventana_edicion.resizable(False, False)
            ventana_edicion.grab_set()

            #edicion
            entrada_edicion = ctk.CTkEntry(
                ventana_edicion,
                width=350,
                height=35,
                corner_radius=10,
                font=("Times New Roman", 14)
            )
            entrada_edicion.pack(pady=15)
            entrada_edicion.insert(0, descripcion)

            #guardar
            def guardar_cambios():
                nueva_descripcion = entrada_edicion.get().strip()
                if nueva_descripcion:
                    try:
                        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
                        cursor = conn.cursor()
                        cursor.execute(
                            "UPDATE fechas_seleccionadas SET descripcion=? WHERE id=?",
                            (nueva_descripcion, recordatorio_id)
                        )
                        conn.commit()
                        conn.close()
                        self.cargar_lista_recordatorios()
                        ventana_edicion.destroy()
                    except Exception as e:
                        print("Error al guardar:", e)

            ctk.CTkButton(
                ventana_edicion,
                text="Guardar",
                command=guardar_cambios
            ).pack()

        except Exception as e:
            print("Error al editar:", e)
    
    def borrar_recordatorio(self):
        "Elimina el recordatorio seleccionado"
        if not self.recordatorio_seleccionado:
            CTkMessagebox(
                title="Sin selección", 
                message="Primero selecciona un recordatorio de la lista.",
                icon="warning", 
                option_1="Ok"
            )
            return

        #Confirmacion
        msg = CTkMessagebox(
            title="Confirmar borrado",
            message="¿Estás seguro de que quieres borrar este recordatorio?",
            icon="question",
            option_1="Cancelar",
            option_2="Borrar"
        )
        
        if msg.get() == "Borrar":
            try:
                conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
                cursor = conn.cursor()
                
                # Primero obtenemos la fecha para quitar el resaltado
                cursor.execute(
                    "SELECT fecha FROM fechas_seleccionadas WHERE id=?",
                    (self.recordatorio_seleccionado,)
                )
                fecha_db = cursor.fetchone()[0]
                
                # Luego borramos el recordatorio
                cursor.execute(
                    "DELETE FROM fechas_seleccionadas WHERE id=?",
                    (self.recordatorio_seleccionado,)
                )
                conn.commit()
                conn.close()
                
                #Quitar el resaltado del calendario
                try:
                    fecha_datetime = datetime.strptime(fecha_db, "%Y-%m-%d").date()
                    for event in self.calendario.calevent_get():
                        if self.calendario.calevent_cget(event, 'date') == fecha_datetime:
                            self.calendario.calevent_remove(event)
                            break
                except Exception as e:
                    print("Error al quitar resaltado:", e)
                
                # Actualizar la lista
                self.recordatorio_seleccionado = None
                self.cargar_lista_recordatorios()
                
                CTkMessagebox(
                    title="Éxito", 
                    message="Recordatorio borrado correctamente.", 
                    icon="info", 
                    option_1="Ok"
                )
                
            except Exception as e:
                print("Error al borrar:", e)
                CTkMessagebox(
                    title="Error", 
                    message="Error al borrar el recordatorio.", 
                    icon="error", 
                    option_1="Ok"
                )


    def editar_recordatorio(self):
        if not self.recordatorio_seleccionado:
            CTkMessagebox(
                title="Sin selección", 
                message="Primero selecciona un recordatorio de la lista.",
                icon="warning", 
                option_1="Ok"
            )
            return

        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT fecha, descripcion FROM fechas_seleccionadas WHERE id=?",
                (self.recordatorio_seleccionado,)
            )
            fila = cursor.fetchone()
            conn.close()

            if fila:
                fecha_db, descripcion = fila
                # Convertir fecha al formato mostrado (DD/MM/YYYY)
                fecha = datetime.strptime(fecha_db, "%Y-%m-%d").strftime("%d/%m/%Y")
                
                # Crear ventana emergente para editar
                self.ventana_editar = ctk.CTkToplevel(self.panel_principal)
                self.ventana_editar.title("Editar Recordatorio")
                self.ventana_editar.geometry("400x200")
                self.ventana_editar.resizable(False, False)
                self.ventana_editar.grab_set()  # Hacerla modal
                
                # Etiqueta con la fecha (solo lectura)
                ctk.CTkLabel(
                    self.ventana_editar,
                    text=f"Fecha: {fecha}",
                    font=("Times New Roman", 14)
                ).pack(pady=(15, 5))
                
                # Campo para editar la descripción
                self.entrada_editar = ctk.CTkEntry(
                    self.ventana_editar,
                    width=350,
                    height=35,
                    corner_radius=10,
                    font=("Times New Roman", 14)
                )
                self.entrada_editar.pack(pady=10)
                self.entrada_editar.insert(0, descripcion)
                
                # Botón para guardar cambios
                ctk.CTkButton(
                    self.ventana_editar,
                    text="Guardar Cambios",
                    width=150,
                    height=35,
                    corner_radius=10,
                    font=("Times New Roman", 14),
                    command=self.guardar_cambios_edicion
                ).pack(pady=10)
                
            else:
                CTkMessagebox(
                    title="No encontrado", 
                    message="No se encontró el recordatorio.", 
                    icon="warning", 
                    option_1="Ok"
                )

        except Exception as e:
            print("Error al editar:", e)
            CTkMessagebox(
                title="Error", 
                message="Error al cargar el recordatorio.", 
                icon="error", 
                option_1="Ok"
            )

    def guardar_cambios_edicion(self):
        nueva_descripcion = self.entrada_editar.get().strip()
        
        if not nueva_descripcion:
            CTkMessagebox(
                title="Campo vacío", 
                message="La descripción no puede estar vacía.",
                icon="warning", 
                option_1="Ok"
            )
            return
        
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE fechas_seleccionadas SET descripcion=? WHERE id=?",
                (nueva_descripcion, self.recordatorio_seleccionado)
            )
            conn.commit()
            conn.close()
            
            CTkMessagebox(
                title="Éxito", 
                message="Recordatorio actualizado correctamente.", 
                icon="info", 
                option_1="Ok"
            )
            
            # Cerrar ventana de edición y actualizar lista
            self.ventana_editar.destroy()
            self.cargar_lista_recordatorios()
            
        except Exception as e:
            print("Error al guardar cambios:", e)
            CTkMessagebox(
                title="Error", 
                message="Error al actualizar el recordatorio.", 
                icon="error", 
                option_1="Ok"
            )
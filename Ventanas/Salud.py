from Ventanas.Ventana_interfaz import New_ventana
from Ventanas.update_peso import Peso
from Ventanas.pulsaciones import Pulsaciones
from tkinter import messagebox
from util.colores import *
import customtkinter as ctk
import sqlite3
from CTkMessagebox import CTkMessagebox
from datetime import datetime
from Clases.reporte import GeneradorReporte
from Sub.PDF import GeneradorPDF
from Sub.Excel import GeneradorExcel
from Sub.Texto import GeneradorTexto

class Salud(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color, 'salud')
        self.add_widget_salud()
        self.vasitos_mostrados()
        self.update_health_metrics()
        self.mensage("Esta es la pestaña de Salud, aqui podras gestionar tu peso actual, medir tus pulsaciones, ver tu IMC (indice de masa corporal) al igual que tu TMC (tasa metabolica basal)", "Salud")

    def mostrar_advertencia(self):
        CTkMessagebox(title="Salud", message="Esta es la pestaña de Salud, aqui podras gestionar tu peso actual, medir tus pulsaciones, ver tu IMC (indice de masa corporal) al igual que tu TMC (tasa metabolica basal)", icon='info', option_1="Ok")

    def add_widget_salud(self):
        # Botón "Actualizar Peso"
        self.btn_actualizar_peso = ctk.CTkButton(self.sub, text="Actualizar Peso", width=250, height=50, fg_color=verde_boton, font=("Arial", 18, 'bold'),
                                                 hover_color=verde_oscuro, text_color=azul_medio_oscuro, command=self.actualizar_peso, corner_radius=20)
        self.btn_actualizar_peso.place(x=50, y=50)

        self.boton_ayuda = ctk.CTkButton(self.sub, text="i",
                                         command=self.mostrar_advertencia,
                                         corner_radius=20,
                                         width=30, height=30,
                                         font=("Times New Roman", 25, "italic"),
                                         text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")

        # Botón "Medir pulsaciones"
        self.btn_medir_pulsaciones = ctk.CTkButton(self.sub, text="Medir pulsaciones", width=250, height=50, fg_color=verde_boton, corner_radius=20,
                                                   hover_color=verde_oscuro, text_color=azul_medio_oscuro, command=self.pulsaciones, font=("Arial", 18, 'bold'))
        self.btn_medir_pulsaciones.place(x=50, y=150)

        self.label_imc = ctk.CTkLabel(self.sub, text="IMC:", fg_color=azul_medio_oscuro, text_color=segundo_label, font=("Arial", 18, 'bold'), width=100, height=50)
        self.label_imc.configure(corner_radius=20)
        self.label_imc.place(x=500, y=50)

        self.result_imc = ctk.CTkLabel(self.sub, text="", text_color="white", font=("Arial", 18, 'bold'), width=100, height=50)
        self.result_imc.configure(corner_radius=20)
        self.result_imc.place(x=610, y=50)

        self.label_tmb = ctk.CTkLabel(self.sub, text="TMB:", fg_color=azul_medio_oscuro, text_color=segundo_label, font=("Arial", 18, 'bold'), width=100, height=50)
        self.label_tmb.configure(corner_radius=20)
        self.label_tmb.place(x=500, y=150)
        
        self.result_tmb = ctk.CTkLabel(self.sub, text="", text_color="white", font=("Arial", 18, 'bold'), width=100, height=50)
        self.result_tmb.configure(corner_radius=20)
        self.result_tmb.place(x=610, y=150)

        self.mensaje = ctk.CTkLabel(self.sub, text="", 
                                    text_color="white", font=("Arial", 14))
        self.mensaje.place(x=500, y=100)

        self.mensaje_tbm =ctk.CTkLabel(self.sub, text="", 
                                    text_color="white", font=("Arial", 14))
        self.mensaje_tbm.place(x=500, y=200)

        self.opcion_seleccionada = ctk.StringVar(value="pdf")  # Valor por defecto

        self.menu_opciones = ctk.CTkOptionMenu(
            self.sub,
            values=["pdf", "excel", "texto"],
            variable=self.opcion_seleccionada,
            width=250,
            height=50,
            fg_color=verde_boton,
            button_color=verde_boton,
            button_hover_color=verde_oscuro,
            text_color=azul_medio_oscuro,
            font=("Arial", 18, "bold"),
            dropdown_font=("Arial", 16),
            dropdown_text_color=azul_medio_oscuro
        )
        self.menu_opciones.place(x=50, y=220)  # Ajusta la coordenada según tu layout

        self.boton_generar = ctk.CTkButton(
            self.sub,
            text="Generar reporte",
            width=250,
            height=50,
            fg_color=verde_boton,
            hover_color=verde_oscuro,
            text_color=azul_medio_oscuro,
            corner_radius=20,
            command=self.GeneradorReporte,
            font=("Arial", 18, "bold")
        )
        self.boton_generar.place(x=50, y=290)  # Ajusta la coordenada según necesites




        # Crear los 8 botones redondeados debajo de la barra
        self.botones = []
        self.estado_botones = [False] * 8  # Lista para almacenar el estado de cada botón (False = gris, True = verde)
        # botones vaso de agua
        boton_v_1 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(0))
        boton_v_1.place(x=50, y=400)
        self.botones.append(boton_v_1)
        boton_v_2 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda:  self.toggle_color(1) if self.estado_botones[0] else None)
        boton_v_2.place(x=110, y=400)
        self.botones.append(boton_v_2)
        boton_v_3 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(2) if self.estado_botones[1] else None)
        boton_v_3.place(x=170, y=400)
        self.botones.append(boton_v_3)
        boton_v_4 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(3) if self.estado_botones[2] else None)
        boton_v_4.place(x=230, y=400)
        self.botones.append(boton_v_4)
        boton_v_5 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(4) if self.estado_botones[3] else None)
        boton_v_5.place(x=290, y=400)
        self.botones.append(boton_v_5)
        boton_v_6 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(5) if self.estado_botones[4] else None)
        boton_v_6.place(x=350, y=400)
        self.botones.append(boton_v_6)
        boton_v_7 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(6) if self.estado_botones[5] else None)
        boton_v_7.place(x=410, y=400)
        self.botones.append(boton_v_7)
        boton_v_8 = ctk.CTkButton(self.sub, text="", width=50, height=50, corner_radius=20, fg_color="gray", hover_color=verde_claro,
                                  command=lambda: self.toggle_color(7) if self.estado_botones[6] else None)
        boton_v_8.place(x=470, y=400)
        self.botones.append(boton_v_8)

        # Barra inferior
        self.barra_inferior = ctk.CTkProgressBar(self.sub, width=550, height=40, fg_color="#417156", progress_color="#ade28a")
        self.barra_inferior.place(x=20, y=350)
        self.barra_inferior.set(0.7)

        # Etiquetas de Meta de Calorías y Vasos de Agua
        self.label_meta_calorias = ctk.CTkLabel(self.sub, text="Meta de Calorías x/Meta", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_meta_calorias.place(x=600, y=350)

        self.label_vasos_agua = ctk.CTkLabel(self.sub, text="Vasos de Agua: x", fg_color=None, text_color="black", font=("Arial", 15))
        self.label_vasos_agua.place(x=600, y=420)


    def toggle_color(self, indice):
        if self.estado_botones[indice]:
            self.botones[indice].configure(fg_color="gray")
            self.estado_botones[indice] = False
            self.eliminar_vasitos()
        elif not self.estado_botones[indice] and (indice == 0 or self.estado_botones[indice - 1]):
            self.botones[indice].configure(fg_color=verde_boton)
            self.estado_botones[indice] = True
            self.Insertar_vasitos()

    def Insertar_vasitos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
    
        fecha_actual = datetime.now().strftime("%d-%m-%Y")    
    
        cursor.execute("SELECT cant FROM agua WHERE fecha = ?", (fecha_actual,))
        resultado = cursor.fetchone()
    
        if resultado:  
            nueva_cantidad = resultado[0] + 1
            cursor.execute("UPDATE agua SET cant = ? WHERE fecha = ?", (nueva_cantidad, fecha_actual))
        else:  
            cursor.execute("INSERT INTO agua (fecha, cant) VALUES (?, 1)", (fecha_actual,))
        conn.commit()
        conn.close()
        
    def eliminar_vasitos(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()

        fecha_actual = datetime.now().strftime("%d-%m-%Y")

        cursor.execute("SELECT cant FROM agua WHERE fecha = ?", (fecha_actual,))
        resultado = cursor.fetchone()

        if resultado and resultado[0] > 0:
            nueva_cantidad = resultado[0] - 1
            cursor.execute("UPDATE agua SET cant = ? WHERE fecha = ?", (nueva_cantidad, fecha_actual))

        conn.commit()
        conn.close()

    def vasitos_mostrados(self):
        conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
        cursor = conn.cursor()
        fecha_actual = datetime.now().strftime("%d-%m-%Y")    
        cursor.execute("SELECT cant FROM agua WHERE fecha = ?", (fecha_actual,))
        resultado = cursor.fetchone()
        cantidad_vasos = resultado[0] if resultado else 0
    
        #cambiar el color de los botones a verde si se tomaron los vasitos
        for i in range(cantidad_vasos):
            self.botones[i].configure(fg_color="green")
            self.estado_botones[i] = True
    
        conn.close()
    
    def actualizar_peso(self):
        Peso(self.sub, self.usuario, callback=self.update_health_metrics)

    def get_latest_weight(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT peso FROM peso ORDER BY fecha DESC LIMIT 1")
            result = cursor.fetchone()
            
            if result is None:
                raise ValueError("No se encontró ningún registro de peso")
            
            return result[0]
        except (sqlite3.Error, ValueError) as e:
            print(f"Error al obtener el peso más reciente: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def calcular_imc(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura FROM datos")
            resultado_estatura = cursor.fetchone()
            if resultado_estatura is None:
                raise ValueError("No se encontró la estatura para el usuario")
            estatura = resultado_estatura[0] / 100  # Convertir a metros

            cursor.execute("SELECT peso FROM peso WHERE num = (SELECT MAX(num) FROM peso)")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró ningún registro de peso")
            peso = resultado_peso[0]

            imc = peso / (estatura ** 2)
            return imc

        except (sqlite3.Error, ValueError) as e:
            print(f"Error al calcular IMC: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def calcular_TMB(self):
        try:
            conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT estatura, edad, genero FROM datos")
            result = cursor.fetchone()
            if result is None:
                raise ValueError("No se encontraron datos del usuario")
            estatura, edad, genero = result
            estatura = estatura  # Convertir a metros

            cursor.execute("SELECT peso FROM peso WHERE num = (SELECT MAX(num) FROM peso)")
            resultado_peso = cursor.fetchone()
            if resultado_peso is None:
                raise ValueError("No se encontró ningún registro de peso")
            peso = resultado_peso[0]

            if genero.lower() in ["hombre", "masculino"]:
                tmb = 66.47 + (13.75 * peso) + (5 * estatura) - (6.76 * edad)
            elif genero.lower() in ["mujer", "femenino"]:
                tmb = 655.1 + (9.56 * peso) + (1.85 * estatura) - (4.68 * edad)
            else:
                raise ValueError("Género no válido")
            
            return tmb

        except (sqlite3.Error, ValueError) as e:
            print(f"Error al calcular TMB: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def update_health_metrics(self):
        imc = self.calcular_imc()
        tmb = self.calcular_TMB()

        imc1 = "Su IMC indica bajo peso"
        imc2 = "Su IMC está dentro del rango saludable"
        imc3 = "Su IMC indica sobrepeso"
        imc4 = "Su IMC se encuentra en el rango de obesidad"

        tbm1 = "Su TMB está algo baja"
        tbm2 = "Su TMB se encuentra en un rango normal"
        tbm3 = "Su TMB es más alta de lo promedio"

        # Cambiar color del IMC
        if imc is not None:
            self.result_imc.configure(text=f"{imc:.2f}")
            if imc < 18.5: 
                self.result_imc.configure(fg_color=riesgo_alto)
                self.mensaje.configure(text = imc1)
            elif 18.5 <= imc < 24.9:  
                self.result_imc.configure(fg_color=riesgo_bajo) 
                self.mensaje.configure(text = imc2)
            elif 25 <= imc < 29.9: 
                self.result_imc.configure(fg_color=riesgo_medio)
                self.mensaje.configure(text = imc3)
            else:  
                self.result_imc.configure(fg_color=riesgo_alto)
                self.mensaje.configure(text = imc4)
        else:
            self.result_imc.configure(text="Error", fg_color="red")  

        # Cambiar color del TMB
        if tmb is not None:
            self.result_tmb.configure(text=f"{tmb:.2f}")
            if tmb < 1200:  
                self.result_tmb.configure(fg_color=riesgo_alto)
                self.mensaje_tbm.configure(text=tbm1)
            elif 1200 <= tmb < 1800:  
                self.result_tmb.configure(fg_color=riesgo_bajo)
                self.mensaje_tbm.configure(text=tbm2) 
            else:  
                self.result_tmb.configure(fg_color=riesgo_alto)
                self.mensaje_tbm.configure(text=tbm3)
        else:
            self.result_tmb.configure(text="Error", fg_color=riesgo_alto) 
        
        self.sub.update()
    
    def pulsaciones(self):
        Pulsaciones(self.sub)

    def GeneradorReporte(self):
        formato = self.opcion_seleccionada.get()

        calcular_imc = self.calcular_imc  
        calcular_TMB = self.calcular_TMB  
        cargar_datos_usuario = self.cargar_datos_usuario

        if formato == "pdf":
            generador = GeneradorPDF(self.usuario, calcular_imc, calcular_TMB, cargar_datos_usuario)
        elif formato == "excel":
            generador = GeneradorExcel(self.usuario, calcular_imc, calcular_TMB, cargar_datos_usuario)
        elif formato == "texto":
            generador = GeneradorTexto(self.usuario, calcular_imc, calcular_TMB, cargar_datos_usuario)
        else:
            CTkMessagebox(title="Error", message="Formato no soportado", icon="cancel")
            return

        generador.generar()

    
    def cargar_datos_usuario(self):
            """Obtiene la edad, el género, la meta de calorías, el nivel de actividad, la altura y el peso más reciente del usuario desde la base de datos."""
            try:
                conn = sqlite3.connect(f"./users/{self.usuario}/alimentos.db")
                cursor = conn.cursor()

                # Obtener datos del usuario, incluyendo la estatura
                cursor.execute("SELECT edad, genero, meta_cal, nivel_actividad, estatura FROM datos WHERE nombre = ?", (self.usuario,))
                user_data = cursor.fetchone()

                # Obtener el peso más reciente
                cursor.execute("SELECT peso, fecha FROM peso ORDER BY fecha DESC LIMIT 1")
                peso_data = cursor.fetchone()
                conn.close()

                if user_data and peso_data:
                    edad, genero, meta_cal, nivel_actividad, estatura = user_data
                    peso, fecha = peso_data  # Fecha y peso más recientes
                    self.obj_calorias_original = meta_cal
                    self.lvl_actividad_original = nivel_actividad
                    return edad, genero, peso, nivel_actividad, meta_cal, estatura
                else:
                    return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"

            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al acceder a la base de datos: {e}")
                return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"

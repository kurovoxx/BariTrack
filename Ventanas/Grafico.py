import customtkinter as ctk
from Ventanas.Ventana_interfaz import New_ventana
from CTkMessagebox import CTkMessagebox
from Sub.Grafico_Calorias import Grafico_Calorias
from Sub.Grafico_Peso import Grafico_Peso
from Sub.Grafico_Agua import Grafico_Agua
from util.colores import *

class Grafico(New_ventana):
    def __init__(self, panel_principal, color):
        super().__init__(panel_principal, color, 'graficos')
        self.panel_principal = panel_principal
        self.add_widget_graficos()
        self.mensage("Esta es la pestaña de Graficos, aqui podras ver graficamente el progreso que has tenido en los dias, podras ver graficos como Calorias vs Tiempo, Peso vs Tiempo, Aguas vs Tiempo", "Grafico")

        # Botón de ayuda
        self.boton_ayuda = ctk.CTkButton(self.panel_principal, text="i",
                                       command=self.mostrar_advertencia,
                                       corner_radius=15,
                                       width=30, height=30,
                                       font=("Times New Roman", 25, "italic"),
                                       text_color="white")
        self.boton_ayuda.place(relx=0.97, rely=0.04, anchor="ne")

    def mostrar_advertencia(self):
        CTkMessagebox(title="Grafico", message="Esta es la pestaña de Graficos, aqui podras ver graficamente el progreso que has tenido en los dias, podras ver graficos como Calorias vs Tiempo, Peso vs Tiempo, Aguas vs Tiempo.", icon='info', option_1="Ok")

    def add_widget_graficos(self):
        tabview = ctk.CTkTabview(self.panel_principal, width=800, height=550,
                               fg_color=gris,
                               bg_color=gris,
                               segmented_button_fg_color=azul_medio_oscuro,
                               segmented_button_selected_color=verde_claro,
                               segmented_button_selected_hover_color=gris,
                               segmented_button_unselected_color=azul_medio_oscuro,
                               segmented_button_unselected_hover_color=verde_claro)
        tabview.place(relx=0.01, rely=0.005, relwidth=1, relheight=1)
        
        # Crear implementaciones concretas
        self.crear_tab_grafico(tabview, "Calorías vs Tiempo", Grafico_Calorias())
        self.crear_tab_grafico(tabview, "Peso vs Tiempo", Grafico_Peso())
        self.crear_tab_grafico(tabview, "Agua vs Tiempo", Grafico_Agua())

    def crear_tab_grafico(self, tabview, nombre, implementacion):
        """Método genérico para crear cualquier pestaña de gráfico"""
        tab = tabview.add(nombre)
        datos = implementacion.obtener_datos(self.usuario)
        implementacion.crear_grafico(tab, datos)
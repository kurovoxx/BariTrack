import sqlite3
import datetime
import customtkinter as ctk

# Para María


def sql_insert(self, nomb, n_cal, sel):
    try:
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()

        if sel == 'Cuantas calorías hay en 100g':
            query = '''
            INSERT INTO alimentos (nombre, calorias_100g) VALUES (?, ?);
            '''
        else:
            query = '''
            INSERT INTO alimentos (nombre, calorias_porcion) VALUES (?, ?);
            '''

        cursor.execute(query, (nomb, n_cal))
        conn.commit()
        print('Alimento insertado con éxito!')

    except sqlite3.Error as error:
        print(f"Error al insertar en la base de datos: {error}")

    finally:
        if conn:
            conn.close()


# Para Hector

# implemetar con su metodología de conexión sql

def insert(self):
    conn = sqlite3.connect('alimentos.db')
    cursor = conn.cursor()
    query = '''
            INSERT INTO consumo_diario (fecha, nombre) VALUES (?, ?);
            '''
    cursor.execute(query, (datetime.now().strftime('%d-%m-%Y'), self.seleccionar.get()))
    conn.commit()
    conn.close()
    self.ultimo_alimento.configure(text=self.get_ultimo_insertado())
    print('Alimento registrado!')
    try:
        self.get_total_calorias(str(datetime.now().strftime('%d-%m-%Y')))
    except:
        pass


def get_ultimo_insertado(self):
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()
        query = "SELECT nombre FROM consumo_diario WHERE id = (SELECT MAX(id) FROM consumo_diario);"
        cursor.execute(query)
        ultimo = str(cursor.fetchone())
        conn.commit()
        conn.close()
        if ultimo is None:
            return 'Agrega un alimento!'

        return f'El último alimento registrado fue {ultimo[2:-3]}'

def get_total_calorias(self, fecha):
        conn = sqlite3.connect('alimentos.db')
        cursor = conn.cursor()
        query_2 = '''
        SELECT fecha, SUM(alimentos.calorias_100g) AS total_calorias
        FROM consumo_diario
        JOIN alimentos ON consumo_diario.nombre = alimentos.nombre
        WHERE fecha = ?
        GROUP BY fecha;
        '''
        cursor.execute(query_2, (fecha,))
        primer = cursor.fetchall()
        try:
            if primer[0][1] is None:
                primer = [(0, 0)]
        except:
            primer = [(0, 0)]
        query_3 = '''
        SELECT fecha, SUM(alimentos.calorias_porcion) AS total_calorias
        FROM consumo_diario
        JOIN alimentos ON consumo_diario.nombre = alimentos.nombre
        WHERE fecha = ?
        GROUP BY fecha;
        '''
        cursor.execute(query_3, (fecha,))
        segundo = cursor.fetchall()
        try:
            if segundo[0][1] is None:
                segundo = [(0, 0)]
        except:
            segundo = [(0, 0)]
        calorias_totales = primer[0][1] + segundo[0][1]
        conn.commit()
        conn.close()
        self.total_calorias_1 = ctk.CTkLabel(self.sub, text='Hoy se han consumido', text_color='black',
                                             font=('arial', 25))
        self.total_calorias_1.place(x=730, y=60)
        self.total_calorias_2 = ctk.CTkLabel(self.sub, text=str(calorias_totales) + ' calorías.', text_color='black',
                                             font=('arial', 25))
        self.total_calorias_2.place(x=730, y=110)


# para obtener los usuarios (devuelve una lista con los usuarios)

def leer_usuarios(filename='usuarios_registrados.txt'):
    try:
        with open(filename, 'r') as file:
            # Leer todas las líneas del archivo y eliminar los saltos de línea
            usuarios = [linea.strip() for linea in file.readlines()]
        return usuarios
    except FileNotFoundError:
        # Manejar el caso en que el archivo no exista
        print(f"El archivo {filename} no existe.")
        return []


'''
from tkinter import ttk

style = ttk.Style()
style.configure('Treeview', font=('Arial', 12))
style.configure('Treeview.Heading', font=('Arial', 12))
'''

self.btn_registro = tk.Button(self.menu_lateral)
self.btn_agregar = tk.Button(self.menu_lateral)
self.btn_grafico = tk.Button(self.menu_lateral)
self.btn_historial = tk.Button(self.menu_lateral)
self.btn_en_contruccion = tk.Button(self.menu_lateral)
        
buttons_info = [
            ("Registrar Alimento", "\uf109", self.btn_registro, self.abrir_registro_alimento),
            ("Agregar Alimento", "\uf007", self.btn_agregar, self.abrir_agregar_alimento),
            ("Gráfico", "\uf03e", self.btn_grafico, self.abrir_grafico),
            ("Historial", "\uf129", self.btn_historial, self.abrir_historial),
            ("Settings", "\uf013", self.btn_en_contruccion, self.abrir_configuracion)
        ]
        
for text, icon, button, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)  
from util.query import obtener_valor
from Usuario import Usuario


class Usuario:
    def __init__(self) -> None:
        self.nombre = obtener_valor("usuarios.db", 'current_user', 'nombre')
        self.init_contrasena()
        self.init_edad()
        self.init_peso()
        self.init_sexo()
        self.init_lvl_act_fisica()
        self.init_meta_calorias()
        self.init_altura()

    def init_contrasena(self):
        self.contrasena = None

    def init_edad(self):
        self.edad = None

    def init_peso(self):
        self.peso = None

    def init_sexo(self):
        self.sexo = None

    def init_lvl_act_fisica(self):
        self.lvl_act_fisica = None

    def init_meta_calorias(self):
        self.meta_calorias = None

    def init_altura(self):
        self.altura = None

    def init_alimentos(self):
        pass


'''Escribir función para querys en /util'''

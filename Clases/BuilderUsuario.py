from query import obtener_valor
from Usuario import Usuario
from InterfaceBuilder import Builder


for i in range(100):
    print(obtener_valor("usuarios.db", 'current_user', 'nombre'))

class BuilderUsuario(Builder):
    def __init__(self) -> None:
        self.nombre = obtener_valor("usuarios.db", 'current_user', 'nombre')
        self.db = f"./users/{self.nombre}/alimentos.db"
        #self.contrasena = obtener_valor(self.db, 'datos', 'contrasena')
        self.edad = obtener_valor(self.db, 'datos', 'edad')
        self.peso = obtener_valor(self.db, 'peso', 'peso')
        self.sexo = obtener_valor(self.db, 'datos', 'genero')
        self.lvl_act_fisica = obtener_valor(self.db, 'datos', 'nivel_actividad')
        self.meta_calorias = obtener_valor(self.db, 'datos', 'meta_cal')
        self.estatura = obtener_valor(self.db, 'datos', 'estatura')

    def crear_usuario(self):
        return Usuario(self.nombre, self.edad, self.peso, self.sexo, self.lvl_act_fisica, self.meta_calorias, self.estatura)

# Instancia del builder
mi_user = BuilderUsuario()

# Crear el usuario (instancia de Usuario)
user = mi_user.crear_usuario()

# Usar métodos del usuario
user.test()

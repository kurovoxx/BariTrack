class Usuario:
    def __init__(self, nombre, edad, peso, sexo, lvl_act_fisica, meta_calorias, estatura) -> None:
        self.nombre = nombre
        #self.contrasena = contrasena
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        self.lvl_act_fisica = lvl_act_fisica
        self.meta_calorias = meta_calorias
        self.estatura = estatura

    def test(self):
        print('olo')
    
    def test2(self):
        print(self.nombre)


'''Escribir función para querys en /util'''

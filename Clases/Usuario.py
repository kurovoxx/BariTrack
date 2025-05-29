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

    def crear_memento(self) -> MementoUsuario:
        estado = {
            'nombre': self.nombre,
            'edad': self.edad,
            'sexo': self.sexo,
            'lvl_act_fisica': self.lvl_act_fisica,
            'meta_calorias': self.meta_calorias,
            'estatura': self.estatura
        }
        return MementoUsuario(estado)

    def restaurar_estado(self, memento: MementoUsuario):
        estado = memento.get_estado()
        self.nombre = estado['nombre']
        self.edad = estado['edad']
        self.sexo = estado['sexo']
        self.lvl_act_fisica = estado['lvl_act_fisica']
        self.meta_calorias = meta_calorias['meta_calorias']
        self.estatura = estatura['estatura']




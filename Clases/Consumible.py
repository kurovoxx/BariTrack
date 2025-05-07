class Consumible:
    def __init__(self) -> None:
        self.init_nombre_cons()
        self.init_cantidad()
        self.init_tipo_medida()

    def init_nombre_cons(self):
        self.nombre_cons = None

    def init_cantidad(self):
        self.cantidad = None

    def init_tipo_medida(self):
        self.tipo_medida = None

from Consumible import Consumible

class Alimentos:
    def __init__(self) -> None:
        self.lista_consumibles = []
    
    def add_consumibles(self, c: Consumible):
        self.lista_consumibles.append(c)

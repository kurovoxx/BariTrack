from abc import ABC, abstractmethod

class Consumible(ABC):
    def __init__(self, nombre_cons, cant_cons, tipo_medida, tipo):
        self.nombre_cons = nombre_cons
        self.cant_consumible = cant_cons
        self.tipo_medida = tipo_medida
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre_cons} ({self.tipo}): {self.cant_consumible}{self.tipo_medida}"

class Carne(Consumible):
    def __init__(self, nombre, cantidad, unidad):
        super().__init__(nombre, cantidad, unidad, "Carne")

class Verdura(Consumible):
    def __init__(self, nombre, cantidad, unidad):
        super().__init__(nombre, cantidad, unidad, "Verdura")

class Liquido(Consumible):
    def __init__(self, nombre, cantidad, unidad):
        super().__init__(nombre, cantidad, unidad, "Líquido")

class Avena(Consumible):
    def __init__(self, nombre, cantidad, unidad):
        super().__init__(nombre, cantidad, unidad, "Avena")

# Clase abstracta de Factory
class ConsumibleFactory(ABC):
    @abstractmethod
    def crear_consumible(self, nombre, cantidad, unidad) -> Consumible:
        pass

# Fábricas concretas
class CarneFactory(ConsumibleFactory):
    def crear_consumible(self, nombre, cantidad, unidad) -> Carne:
        return Carne(nombre, cantidad, unidad)

class VerduraFactory(ConsumibleFactory):
    def crear_consumible(self, nombre, cantidad, unidad) -> Verdura:
        return Verdura(nombre, cantidad, unidad)

class LiquidoFactory(ConsumibleFactory):
    def crear_consumible(self, nombre, cantidad, unidad) -> Liquido:
        return Liquido(nombre, cantidad, unidad)

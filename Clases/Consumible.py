from abc import ABC, abstractmethod
from typing import List

# Componente abstracto (Component)
class Consumible(ABC):
    def __init__(self, nombre_cons: str, cant_consumible: int, tipo_medida: str):
        self.nombre_cons = nombre_cons
        self.cant_consumible = cant_consumible
        self.tipo_medida = tipo_medida
    
    @abstractmethod
    def edit_nombre(self, nuevo_nombre: str):
        pass
    
    @abstractmethod
    def actualizar_cantidad(self, nueva_cantidad: int):
        pass
    
    @abstractmethod
    def calcular_medida(self) -> float:
        pass
    
    @abstractmethod
    def clone(self):
        pass

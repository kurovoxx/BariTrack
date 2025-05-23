from Consumible import Consumible


class Solido(Consumible):
    def __init__(self, nombre_cons: str, cant_consumible: int, tipo_medida: str = "gramos"):
        super().__init__(nombre_cons, cant_consumible, tipo_medida)
    
    def edit_nombre(self, nuevo_nombre: str):
        self.nombre_cons = nuevo_nombre
    
    def actualizar_cantidad(self, nueva_cantidad: int):
        self.cant_consumible = nueva_cantidad
    
    def calcular_medida(self) -> float:
        """Calcula la medida en gramos para sólidos"""
        return float(self.cant_consumible)
    
    def __str__(self):
        return f"Sólido: {self.nombre_cons} - {self.cant_consumible} {self.tipo_medida}"
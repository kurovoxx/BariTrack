from Consumible import Consumible


class Liquido(Consumible):
    def __init__(self, nombre_cons: str, cant_consumible: int, tipo_medida: str = "ml"):
        super().__init__(nombre_cons, cant_consumible, tipo_medida)
    
    def edit_nombre(self, nuevo_nombre: str):
        self.nombre_cons = nuevo_nombre
    
    def actualizar_cantidad(self, nueva_cantidad: int):
        self.cant_consumible = nueva_cantidad
    
    def calcular_medida(self) -> float:
        """Calcula la medida en mililitros para líquidos"""
        return float(self.cant_consumible)
    
    def calcular_litro(self, cant) -> float:
        """Convierte a litros"""
        cantidad = cant if cant is not None else self.cant_consumible
        return cantidad / 1000.0
    
    def calcular_onza(self, cant) -> float:
        """Convierte a onzas fluidas"""
        cantidad = cant if cant is not None else self.cant_consumible
        return cantidad / 29.5735  # 1 onza fluida = 29.5735 ml
    
    
    def __str__(self):
        return f"Líquido: {self.nombre_cons} - {self.cant_consumible} {self.tipo_medida}"
from Consumible import Consumible
from Solido import Solido
from Liquido import Liquido

class Alimentos:
    def __init__(self):
        self.lista_consumibles = []
    
    def add_consumibles(self, consumible: Consumible):
        """Agrega un consumible a la lista"""
        self.lista_consumibles.append(consumible)
    
    def eliminar_consumible(self, nombre: str):
        """Elimina un consumible por nombre"""
        self.lista_consumibles = [c for c in self.lista_consumibles if c.nombre_cons != nombre]
    
    def clonar(self):
        """Clona toda la lista de alimentos"""
        nuevo_alimentos = Alimentos()
        for consumible in self.lista_consumibles:
            nuevo_alimentos.add_consumibles(consumible.clone())
        return nuevo_alimentos
    
    def calcular_medida_total(self) -> dict:
        """Calcula las medidas totales separadas por tipo"""
        total_solidos = 0.0
        total_liquidos = 0.0
        
        for consumible in self.lista_consumibles:
            if isinstance(consumible, Solido):
                total_solidos += consumible.calcular_medida()
            elif isinstance(consumible, Liquido):
                total_liquidos += consumible.calcular_medida()
        
        return {
            "solidos_gramos": total_solidos,
            "liquidos_ml": total_liquidos,
            "liquidos_litros": total_liquidos / 1000.0
        }
    
    def buscar_por_nombre(self, nombre: str):
        """Busca un consumible por nombre"""
        for consumible in self.lista_consumibles:
            if consumible.nombre_cons == nombre:
                return consumible
        return None
    
    def listar_consumibles(self):
        """Lista todos los consumibles"""
        if not self.lista_consumibles:
            print("No hay consumibles en la lista")
            return
        
        print("=== Lista de Consumibles ===")
        for i, consumible in enumerate(self.lista_consumibles, 1):
            print(f"{i}. {consumible}")
    
    def __len__(self):
        return len(self.lista_consumibles)
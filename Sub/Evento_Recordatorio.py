from Clases.EventoDecorator import EventoDecorator
from datetime import timedelta

class EventoConRecordatorio(EventoDecorator):
    def __init__(self, evento, dias_antes: int):  # Cambiado para aceptar Evento o EventoDecorator
        if not hasattr(evento, 'fecha') or not hasattr(evento, 'mensaje'):
            raise ValueError("El evento debe tener atributos 'fecha' y 'mensaje'")
        super().__init__(evento)
        self.dias_antes = dias_antes
    
    def mostrar(self) -> str:
        try:
            fecha_recordatorio = self.fecha - timedelta(days=self.dias_antes)
            return f"{super().mostrar()} (Recordatorio: {fecha_recordatorio.strftime('%d/%m/%Y')})"
        except Exception as e:
            print(f"Error en mostrar(): {e}")
            return super().mostrar()
    
    def to_dict(self) -> dict:
        try:
            base_dict = super().to_dict()
            base_dict.update({
                'tipo': 'con_recordatorio',
                'dias_antes': self.dias_antes
            })
            return base_dict
        except Exception as e:
            print(f"Error en to_dict(): {e}")
            return {}
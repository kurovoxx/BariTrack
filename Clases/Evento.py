from datetime import date

class Evento:
    def __init__(self, fecha: date, mensaje: str):
        self.fecha = fecha
        self.mensaje = mensaje
    
    def mostrar(self) -> str:
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.mensaje}"
    
    def to_dict(self) -> dict:
        return {
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'mensaje': self.mensaje,
            'tipo': 'base'
        }
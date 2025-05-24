from .Evento import Evento

class EventoDecorator:
    def __init__(self, evento: Evento):
        self._evento = evento
    
    @property
    def fecha(self):
        return self._evento.fecha
    
    @property
    def mensaje(self):
        return self._evento.mensaje
    
    def mostrar(self) -> str:
        return self._evento.mostrar()
    
    def to_dict(self) -> dict:
        return self._evento.to_dict()
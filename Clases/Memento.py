from Usuario import Usuario

class MementoUsuario:
    def __init__(self, estado: dict):
        self._estado = estado.copy()

    def get_estado(self) -> dict:
        return self._estado.copy()


class UsuarioCaretaker:
    def __init__(self):
        self._historial = []

    def guardar_memento(self, memento):
        self._historial.append(memento)

    def deshacer(self):
        if self._historial:
            return self._historial.pop()
        return None


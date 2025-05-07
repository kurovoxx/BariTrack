class Usuarios:
    def __init__(self, new_user) -> None:
        self.lista_users = []
        self.current_user = None
        self.init_lista_users()

    def init_lista_users(self):
        '''query para llenar la lista con los usuarios'''
        pass

    def set_current_user(self, u):
        self.current_user = u
        '''código para cambiar el usuario actual en usuarios.db'''

    def add_user(self, u):
        self.lista_users.append(u)

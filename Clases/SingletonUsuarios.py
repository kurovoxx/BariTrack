import sqlite3
from CTkMessagebox import CTkMessagebox

class Usuarios:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Usuarios, cls).__new__(cls)
        return cls._instance

    def __init__(self, new_user=None) -> None:
        if hasattr(self, "_initialized"):
            return
        self.lista_users = []
        self.current_user = None
        self.init_lista_users()
        self._initialized = True

    def init_lista_users(self):
        self.lista_users = self.obtener_usuarios()

    def set_current_user(self, u):
        self.current_user = u

    def get_current_user(self):
        return self.current_user

    def add_user(self, u):
        self.lista_users.append(u)

    def insertar_usuario(self, nombre: str, contra: str):
        try:
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()

            query = "INSERT INTO users (nombre, contra) VALUES (?, ?)"
            cursor.execute(query, (nombre, contra))
            conn.commit()

            # Actualizamos la lista interna de usuarios
            self.lista_users.append(nombre)

            CTkMessagebox(
                title="Éxito",
                message="Se ha registrado correctamente",
                icon='check',
                option_1="Ok"
            )

        except sqlite3.IntegrityError:
            CTkMessagebox(
                title="Advertencia",
                message="Nombre de usuario ocupado.",
                icon='warning',
                option_1="Ok"
            )

        finally:
            conn.close()

    def obtener_usuarios(self):
        try:
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM users")
            return [u[0] for u in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al obtener los usuarios: {e}")
            return []
        finally:
            conn.close()


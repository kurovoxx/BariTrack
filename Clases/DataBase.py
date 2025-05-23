import sqlite3

class DataBase:
    def __init__(self, route):
        self.route = route
        self.conn = None
        self.cursor = None

    def conectar(self):
        self.conn = sqlite3.connect(self.route)
        self.cursor = self.conn.cursor()

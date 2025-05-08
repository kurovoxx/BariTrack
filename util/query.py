import sqlite3


def obtener_valor(bd: str, tabla: str, campo: str, where_clause='1'):
    conn = sqlite3.connect(bd)
    cursor = conn.cursor()

    query = f"SELECT {campo} FROM {tabla} WHERE {where_clause} LIMIT 1"
    cursor.execute(query)

    resultado = cursor.fetchone()
    conn.close()

    return str(resultado[0]) if resultado else None

# ejemplo de uso
'''estatura = obtener_valor(bd="./users/Test1/alimentos.db",
                         tabla='datos', campo='estatura')
print(estatura)'''

def obtener_valores():
    pass
    # debe retornar un array de valores que cumplan con una clausala WHERE
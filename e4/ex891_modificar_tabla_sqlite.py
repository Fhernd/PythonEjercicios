# Ejercicio 891: Modificar con ALTER TABLE una tabla en una base de datos tipo SQLite.

import sqlite3

def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
    
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()

def modificar_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(sql)

    conexion.commit()

conexion = crear_conexion('Parte001/usuarios_891.db')

sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)

sql = "ALTER TABLE usuario ADD COLUMN email TEXT NOT NULL DEFAULT '@';"

modificar_tabla(conexion, sql)

if conexion:
    conexion.close()

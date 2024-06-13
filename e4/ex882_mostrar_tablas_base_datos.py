# Ejercicio 882: Mostrar las tablas que se han creado en una base de datos SQLite.

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

def mostrar_tablas(conexion):
    sql = "SELECT name FROM sqlite_master WHERE type='table';"

    cursor = conexion.cursor()
    cursor.execute(sql)
    tablas = cursor.fetchall()

    for t in tablas:
        print(t[0])

conexion = crear_conexion('Parte001/usuarios.db')

sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)

sql = """
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
"""
crear_tabla(conexion, sql)

mostrar_tablas(conexion)

if conexion:
    conexion.close()

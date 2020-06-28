# Ejercicio 892: Crear una copia de seguridad de una base de datos tipo SQLite.

import sqlite3
import io

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

def insertar_productos(conexion):
    sql = """
    INSERT INTO producto VALUES (2001, 'Mouse', 'Mouse inalámbrico', 70000);
    INSERT INTO producto VALUES (2002, 'Teclado', 'Teclado gamer', 190000);
    INSERT INTO producto VALUES (2003, 'Monitor', 'Monitor LED', 700000);
    INSERT INTO producto VALUES (2004, 'Parlantes', 'Parlantes 5.1', 400000);
    INSERT INTO producto VALUES (2005, 'Smartphone', 'Smartphone Android', 800000);
    """

    cursor = conexion.cursor()
    cursor.executescript(sql)

    conexion.commit()

def crear_copia_seguridad(conexion, archivo):
    with io.open(archivo, 'w') as f:
        for d in conexion.iterdump():
            f.write('%s\n' % d)

conexion = crear_conexion('Parte001/usuarios_892.db')

sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL
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

print('Tablas existentes en la base de datos:')
mostrar_tablas(conexion)

print()

print('Se van a insertar varios registros en la tabla `producto`...')
insertar_productos(conexion)

print()

archivo_copia = 'Parte001/copia_seguridad_usuarios.sql'

crear_copia_seguridad(conexion, archivo_copia)

if conexion:
    conexion.close()

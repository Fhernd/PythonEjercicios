# Ejercicio 897: Insertar una imagen en una columna tipo BLOB en una base de datos tipo SQLite.

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

def convertir_a_binario(foto):
    with open(foto, 'rb') as f:
        blob = f.read()
    
    return blob

def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, foto) VALUES (?, ?, ?, ?);'

    foto_binario = convertir_a_binario(usuario[-1])
    usuario = (usuario[0], usuario[1], usuario[2], foto_binario)

    cursor = conexion.cursor()
    cursor.execute(sql, usuario)

    conexion.commit()

conexion = crear_conexion('Parte001/usuarios_897.db')

sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    foto BLOB NOT NULL
);
"""
crear_tabla(conexion, sql)

print()

foto_archivo = 'Parte001/foto.png'
usuario = ('Germán', 'gaoojs', 'gaoojs@mail.co', foto_archivo)

crear_usuario(conexion, usuario)

print('El usuario se ha creado de forma satisfactoria.')

if conexion:
    conexion.close()

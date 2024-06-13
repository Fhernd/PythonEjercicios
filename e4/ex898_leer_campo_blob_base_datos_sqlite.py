# Ejercicio 898: Leer una columna tipo BLOB desde una base de datos SQLite.

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

def guardar_foto(id_usuario, foto):
    with open('Parte001/foto_{}.png'.format(id_usuario), 'wb') as f:
        f.write(foto)

def leer_usuario(conexion, id_usuario):
    sql = 'SELECT * FROM usuario WHERE id = ?;'

    cursor = conexion.cursor()
    cursor.execute(sql, (id_usuario, ))

    usuarios = cursor.fetchall()

    for u in usuarios:
        print('%d - %s' % (u[0], u[1]))
        guardar_foto(u[0], u[-1])

conexion = crear_conexion('Parte001/usuarios_898.db')

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

print()

leer_usuario(conexion, 1)

print('Se han leído los datos del usuario con ID:', 1)

if conexion:
    conexion.close()

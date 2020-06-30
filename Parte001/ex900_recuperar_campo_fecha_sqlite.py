# Ejercicio 900: Recuperar un campo tipo fecha (TIMESTAMP) desde una tabla de una base de datos SQLite.

import sqlite3
import datetime

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

def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave, email, fecha_registro) VALUES (?, ?, ?, ?);'

    cursor = conexion.cursor()
    cursor.execute(sql, usuario)

    conexion.commit()

def obtener_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'

    cursor = conexion.cursor()
    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for u in usuarios:
        print('ID:', u[0])
        print('Nombre:', u[1])
        print('Fecha registro:', u[-1])
        print('Fecha registro (tipo de dato):', type(u[-1]))
        # 2020-06-30 17:44:27.634409
        fecha = datetime.datetime.strptime(u[-1], '%Y-%m-%d %H:%M:%S.%f')
        print('Tipo fecha:', type(fecha))
        print()

conexion = crear_conexion('Parte001/usuarios_900.db')

sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_registro TIMESTAMP NOT NULL
);
"""
crear_tabla(conexion, sql)

nombre = 'Daniela'
clave = 'danny'
email = 'danny@mail.co'
fecha_registro = datetime.datetime.now()

usuario = (nombre, clave,  email, fecha_registro)

crear_usuario(conexion, usuario)

print('Se ha creado un nuevo registro en la tabla usuario.')

print()

obtener_usuarios(conexion)

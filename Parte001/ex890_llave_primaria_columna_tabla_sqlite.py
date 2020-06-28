# Ejercicio 890: Crear una columna como llave primaria autoincremental en una base de datos tipo SQLite.

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

def crear_usuario(conexion, usuario):
    sql = 'INSERT INTO usuario (nombre, clave) VALUES (?, ?);'

    cursor = conexion.cursor()
    cursor.execute(sql, usuario)

    conexion.commit()

def mostrar_usuarios(conexion):
    sql = 'SELECT * FROM usuario;'

    cursor = conexion.cursor()
    cursor.execute(sql)

    usuarios = cursor.fetchall()

    for u in usuarios:
        print(u)

def solicitar_datos_usuario():

    while True:
        nombre = input('Ingrese su nombre: ').strip()

        if len(nombre):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para el nombre.')
        
        print()

    while True:
        clave = input('Ingrese su clave: ').strip()

        if len(clave):
            break
        else:
            print('MENSAJE: Debe ingresar una cadena con un valor específico para la clave.')
        
        print()
    
    return nombre, clave

conexion = crear_conexion('Parte001/usuarios_890.db')

sql = """
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""
crear_tabla(conexion, sql)

usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)

print()

usuario = solicitar_datos_usuario()
crear_usuario(conexion, usuario)

print()

mostrar_usuarios(conexion)

if conexion:
    conexion.close()

# Ejercicio 879: Establecer conexión con una base de datos SQLite y obtener su versión.

import sqlite3

try:
    conexion = sqlite3.connect('Parte001/bd_sqlite.db')
    cursor = conexion.cursor()

    print('Se ha creado la base de datos.')
    print('Se ha establecido una conexión con la base de datos.')

    sql = 'SELECT sqlite_version();'
    cursor.execute(sql)
    resultado = cursor.fetchall()

    print()
    print('Versión de SQLite:', resultado[0][0])

    cursor.close()
    
except sqlite3.Error as error:
    print('Se ha producido un error:', error)
finally:
    if conexion:
        conexion.close()
        print('\nLa conexión se ha cerrado de forma satisfactoria.')

# Ejercicio 101: Acceder a una URL e imprimir su contenido HTML.

from http.client import HTTPConnection

url = 'example.com'

conexion = HTTPConnection(url)
conexion.request('GET', '/')

resultado = conexion.getresponse()
contenido = resultado.read()

print(contenido)

# Ejercicio 816: Escribir una lista de cadenas de caracteres en un archivo de texto plano.

def escribir_lista(archivo, lista):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for e in lista:
                f.write('{}\n'.format(e))
    except FileNotFoundError:
        print('El archivo indicado no existe.')


nombre_archivo = 'Parte001/colores.txt'
colores = ['Rojo', 'Verde', 'Azul', 'Blanco', 'Negro', 'Gris', 'Amarillo', 'Morado']

escribir_lista(nombre_archivo, colores)

# Ejercicio 821: Remover los caracteres de salto de línea del contenido de un archivo.

def remover_saltos_linea(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

            lineas = list(map(lambda l: l.rstrip('\n'), lineas))

            return lineas
    except FileNotFoundError:
        print('El archivo especificado no existe.')


resultado = remover_saltos_linea('Parte001/ciudades.txt')

print(resultado)

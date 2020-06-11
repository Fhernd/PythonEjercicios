# Ejercicio 813: Encontrar la palabra más larga almacenada en un archivo de texto plano.

def palabra_mas_larga(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.readline()

            palabras = contenido.split()

            print('Cantidad de palabras:', len(palabras))

            indice = 0
            palabra = palabras[indice]
            longitud = len(palabra)

            for i in range(1, len(palabras)):
                if len(palabras[i]) > longitud:
                    indice = i
                    palabra = palabras[i]
                    longitud = len(palabra)
            
            return palabra, indice

    except FileNotFoundError as e:
        print('El archivo especificado no existe.')


nombre_archivo = 'Parte001/lorem.txt'

resultado = palabra_mas_larga(nombre_archivo)

print(resultado)

# Ejercicio 818: Combinar dos archivos de texto plano en un único archivo.

def combinar_archivos(archivo_1, archivo_2, nuevo_archivo):

    try:
        with open(archivo_1, 'r', encoding='utf-8') as f1, open(archivo_2, 'r', encoding='utf-8') as f2, open(nuevo_archivo, 'w', encoding='utf-8') as f3:
            for l1, l2 in zip(f1, f2):
                f3.write(l1)
                f3.write('\n')
                f3.write(l2)

    except FileNotFoundError:
        print('Uno o ambos archivos no existen.')


faust = 'Parte001/faust.txt'
lorem = 'Parte001/lorem.txt'
nuevo_archivo = 'Parte001/faust_lorem.txt'

combinar_archivos(faust, lorem, nuevo_archivo)

# Ejercicio 823: Generar 26 archivos de texto plano para las letras del abecedario.

# A.txt, B.txt, C.txt, ..., Z.txt

import string, os

def generar_archivos(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    
    for l in string.ascii_uppercase:
        with open(os.path.join(ruta, '%s.txt' % l), 'w', encoding='utf-8') as f:
            f.writelines(l)

ruta = 'Parte001/letras'

generar_archivos(ruta)

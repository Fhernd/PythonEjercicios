# Ejercicio 616: Leer un archivo de texto para contar las ocurrencias de nombres almacenados.

def contar_ocurrencias_nombres(nombre_archivo):
    ocurrencias = {}

    with open(nombre_archivo, 'r') as f:
        nombre = f.readline()

        while nombre:
            nombre = nombre.strip()
            if nombre in ocurrencias:
                ocurrencias[nombre] += 1
            else:
                ocurrencias[nombre] = 1
            
            nombre = f.readline()
    
    return ocurrencias


resultado = contar_ocurrencias_nombres('Parte001/nombres_star_wars.txt')

print(resultado)

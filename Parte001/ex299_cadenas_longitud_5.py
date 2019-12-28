# Ejercicio 299: Crear función para contar el número de cadenas con longitud 5 o mayor.

def contar_cadenas(cadenas):
    contador = 0

    for c in cadenas:
        if len(c) >= 5:
            contador += 1
    
    return contador


palabras = ['Python', 'C#', 'C++', 'JavaScript', 'Java', 'PHP']

print(contar_cadenas(palabras))

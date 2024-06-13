# Ejercicio 370: Usar el método update() para concatenar una lista de diccionarios.

def concatenar_diccionarios(lista):
    diccionarios = {}

    for d in lista:
        diccionarios.update(d)
    
    return diccionarios


dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40, 5: 50}
dict_3 = {6: 60, 7: 70}

lista = [dict_1,  dict_2, dict_3]

resultado = concatenar_diccionarios(lista)

print(resultado)

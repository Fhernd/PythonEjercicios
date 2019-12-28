# Ejercicio 284: Contar el número de caracteres de una cadena en un ciclo while.

def contar_caracteres(cadena):
    contador = 0

    while cadena[contador:]:
        contador += 1
    
    return contador


frase = 'Python v. 3.8.0'
print(len(frase))
print(contar_caracteres(frase))

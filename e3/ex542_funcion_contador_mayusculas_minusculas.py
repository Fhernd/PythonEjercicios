# Ejercicio 542: Crear una función para contar las minúsculas y las mayúsculas de una cadena.

def contador_minusculas_mayusculas(cadena):
    contador = {'minusculas': 0, 'mayusculas': 0}

    for c in cadena:
        if c.isupper():
            contador['mayusculas'] += 1
        elif c.islower():
            contador['minusculas'] += 1
    
    return contador


frase = 'Python es un lenguaje de programación'
print(contador_minusculas_mayusculas(frase))

escritor = 'Fyodor Mijalovich Dostoevskiy'
print(contador_minusculas_mayusculas(escritor))

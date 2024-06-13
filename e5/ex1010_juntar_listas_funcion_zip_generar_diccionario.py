# Ejercicio 1010: Usar la función zip() para fusionar/juntar dos listas en un diccionario.

lenguajes = ['Python', 'Java', 'C#', 'JavaScript']
versiones = ['3.9.2', '15', '9', 'ES6']

# {lenguaje: version}

resultado = dict(zip(lenguajes, versiones))
print(resultado)

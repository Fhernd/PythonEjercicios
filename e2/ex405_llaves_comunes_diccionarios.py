# Ejercicio 405: Listar las llaves comunes entre dos objetos diccionario.

a = {'llave1': 1, 'llave2': 2, 'llave3': 3}
b = {'llave2': 1, 'llave4': 4, 'llave3': 3, 'llave5': 5, 'llave6': 6}

for k in set(a.keys()) & set(b.keys()):
    print(k)

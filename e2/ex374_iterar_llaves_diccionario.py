# Ejercicio 374: Iterar las llaves de un diccionario con el método keys().

lenguajes = {'Python': '3.8.0', 'JavaScript': 'ES6', 'C#': '7.0', 'Java': '12'}

for k in lenguajes.keys():
    print('{} v. {}'.format(k, lenguajes[k]))

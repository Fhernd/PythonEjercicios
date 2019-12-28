# Ejercicio 137: Extraer un único elemento (llave y valor) de un diccionario.

lenguajes = {'Python': '3.8.0', 'Java': '12', 'C#': '8', 'PHP': '7.1.0'}

(lenguaje, version), _, (csharp, vcsharp), _ = lenguajes.items()

print(lenguaje, version)
print(csharp, vcsharp)

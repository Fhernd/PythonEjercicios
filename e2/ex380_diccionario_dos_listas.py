# Ejercicio 380: Mapear dos listas en un único objeto diccionario.

nombres_lenguajes = ['Python', 'JavaScript', 'C#', 'Java']
versiones_lenguajes = ['3.8.0', 'ES6', '7.0', '12']

print(nombres_lenguajes)
print(versiones_lenguajes)

# {'nombre_lenguaje': 'version_lenguaje'}

lenguajes = dict(zip(nombres_lenguajes, versiones_lenguajes))

print(lenguajes)

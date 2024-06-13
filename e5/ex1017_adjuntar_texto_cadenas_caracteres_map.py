# Ejercicio 1017: Usar map() para concatenar texto de forma masiva a una lista de cadenas de caracteres.

nombres = ['Alexander', 'Diana', 'Luisa', 'Pedro', 'Fabián', 'Sebastián', 'Deisy']
print(nombres)

print()

saludo_nombres = list(map(lambda n: f'¡Hola, {n}!', nombres))
print(saludo_nombres)

# Ejercicio 502: Convertir a mayúscula una serie de palabras ingresadas por el usuario.

palabras = []

while True:
    palabra = input()

    if palabra:
        palabras.append(palabra.upper())
    else:
        break

for p in palabras:
    print(p)

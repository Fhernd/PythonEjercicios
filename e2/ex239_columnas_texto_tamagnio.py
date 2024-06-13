# Ejercicio 239: Mostrar texto sobre un número de columnas específicas con textwrap.fill.

from textwrap import fill

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'

print(texto)

print()

print(fill(texto, width=50))

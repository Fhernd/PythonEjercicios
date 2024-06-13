# Ejercicio 242: Agregar indentación a un texto con la función textwrap.fill.

from textwrap import dedent, fill

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'

texto = dedent(texto)

print(texto)

texto = fill(texto, initial_indent='', subsequent_indent=' ' * 4, width=50)

print()

print(texto)

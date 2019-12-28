# Ejercicio 241: Agregar un prefijo a cada línea de un texto con textwrap.indent.

from textwrap import dedent, indent, fill

texto = '   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.'

print(texto)

print()

texto_sin_indentacion = dedent(texto)

texto_con_formato = fill(texto_sin_indentacion, width=60)

print(indent(texto_con_formato, '- '))

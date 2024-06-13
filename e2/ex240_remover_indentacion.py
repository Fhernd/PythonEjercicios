# Ejercicio 240: Remover indentación de un texto por medio de textwrap.dedent.

from textwrap import dedent

texto = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sagittis eget dolor eu ornare. Phasellus id est magna. Quisque sed nisl sit amet felis sagittis ornare. Vivamus sit amet justo neque. Nullam et diam quis felis consequat pellentesque eget eu lorem. Donec nec ante ullamcorper turpis tristique blandit at sit amet libero. Nam accumsan tempus ante, eu ultrices ante gravida id.
'''

print(texto)

texto_sin_indentacion = dedent(texto)

print()

print(texto_sin_indentacion)

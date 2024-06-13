# Ejercicio 344: Imprimir cada sublista de una lista en una nueva línea.

lenguajes = [['Python'], ['JavaScript'], ['Java'], ['PHP'], ['C#']]

resultado = '\n'.join([str(sublista) for sublista in lenguajes])

print(lenguajes)

print()

print(resultado)

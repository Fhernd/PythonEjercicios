# Ejercicio 259: Particionar una cadena de caracteres por la última ocurrencia de un delimitador.

# Solución:

frase = 'Python,PHP,C#,C++,Java,JavaScript,Go'

# rsplit => right_split

lenguajes = frase.rsplit(',', 1)
print(lenguajes)

print()

lenguajes = frase.rsplit(',', 2)
print(lenguajes)

# Ejercicio 715: Crear función para convertir un número entero a un númeral romano.

def conversion_entero_romano(entero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numeral = ''
    i = 0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]

        i += 1
    
    return numeral


print(conversion_entero_romano(123)) # 'CXXIII'

# Prueba de escritorio:
# numeral = 'CXXIII'
# i = 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
# entero = 123, 23, 13, 3, 2, 1, 0

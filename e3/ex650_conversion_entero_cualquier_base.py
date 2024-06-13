# Ejercicio 650: Crear una función recursiva para convertir un entero a cualquier base.

def convertir_entero_base(numero, base):
    conversion_cadena = '0123456789ABCDEF'

    if numero < base:
        return conversion_cadena[numero]
    else:
        return convertir_entero_base(numero//base, base) + conversion_cadena[numero % base]

numero = 13
base = 8
resultado = convertir_entero_base(numero, base)
print(resultado)

# convertir_entero_base(1, 8) + '5' => '1' + '5'
# numero = 1, base = 8
# 

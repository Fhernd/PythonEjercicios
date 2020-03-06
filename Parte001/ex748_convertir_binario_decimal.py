# Ejercicio 748: Crear una función para convertir un número binario en un número decimal.

def es_binario_validio(binario):
    conjunto_bits = set(list(binario))
    
    return ('0' in conjunto_bits or '1' in conjunto_bits) and len(conjunto_bits) in [1, 2]

def convertir_binario_a_decimal(binario):
    if es_binario_validio(binario):
        bits = list(binario)
        valor = 0

        for i in range(len(bits)):
            bit = bits.pop()

            if bit == '1':
                valor += pow(2, i)
        
        return valor
    else:
        raise ValueError('La cadena no representa un número binario válido.')


if __name__ == "__main__":
    binario = '1001' # 9 (10)
    print(convertir_binario_a_decimal(binario))
    
    binario = '10001' # 9 (10)
    print(convertir_binario_a_decimal(binario))

    binario = '11111111' # 9 (10)
    print(convertir_binario_a_decimal(binario))

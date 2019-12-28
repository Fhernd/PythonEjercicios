# Ejercicio 171: Encontrar la cantidad de potencias de 2 a la n en una cadena de caracteres.

# "248163264128"
# "24816"
# "248"

def encontrar_potencias_2(secuencia):
    respuesta = True
    base = 2
    resultado = 2
    grado = 1

    while respuesta:
        if str(resultado) in secuencia:
            grado += 1
            resultado = pow(base, grado)
        else:
            respuesta = False
    
    return grado - 1


print(encontrar_potencias_2('248'))
print(encontrar_potencias_2('24816'))
print(encontrar_potencias_2('248163264128'))

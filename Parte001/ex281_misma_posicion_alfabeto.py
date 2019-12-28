# Ejercicio 281: Contar los caracteres de una frase que ocupan la misma posición del alfabeto.

# Análisis:

# abril
# 1 + 1 = 2

def conteo_caracteres_alfabeto(frase):
    contador = 0

    for i in range(len(frase)):
        if (i == ord(frase[i]) - ord('A')) or (i == ord(frase[i]) - ord('a')):
            contador += 1
    
    return contador


frase = 'abril'
print(conteo_caracteres_alfabeto(frase))

frase = 'algoritmo'
print(conteo_caracteres_alfabeto(frase))

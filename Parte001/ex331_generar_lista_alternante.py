# Ejercicio 331: Generar lista con caracteres alternantes y valores numéricos incrementales.

# [a, b]
# n
# [a1, b1, a2, b2, a3, b3,..., an, bn]

def generar_lista_alternante(caracteres, n):
    lista = ['{}{}'.format(c, i) for i in range(1, n + 1) for c in caracteres]

    return lista


caracteres = ['a', 'b']
n = 10
resultado = generar_lista_alternante(caracteres,  n)

print(resultado)

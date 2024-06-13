# Ejercicio 705: Crear una clase para invertir una frase palabra por palabra.

class OperacionesCadenas:
    def inversion_frases(self, frase):
        resultado = ' '.join(reversed(frase.split()))

        return resultado


frase = 'Python es un lenguaje de programación'
operaciones = OperacionesCadenas()

print(frase)
print(operaciones.inversion_frases(frase))

# Ejercicio 522: Calcular la edad en años de un perro a partir de la edad de una persona.

# Análisis:

# edad_persona <= 2:
# edad perro = edad_persona * 10.5

# edad_persona > 2:
# edad perro = 21 + (edad_persona - 2) * 4

def calcular_edad_perro(edad_persona):
    if edad_persona <= 2:
        return edad_persona * 10.5
    else:
        return 21 + (edad_persona - 2) * 4


edad_persona = int(input('Digite la edad en años de la persona: '))

if edad_persona > 0:
    resultado = calcular_edad_perro(edad_persona)
    print(f'La edad del perro en años sería {resultado}')

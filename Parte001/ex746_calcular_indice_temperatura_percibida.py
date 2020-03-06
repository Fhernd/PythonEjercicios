# Ejercicio 746: Crear una función para calcular el índice de temperatura de sensación (o percibida).

def indice_temperatura_sensacion(t, v):
    """
    Computa el índice de temperatura de sensación o temperatura percibida.
    """
    indice = 13.12 + 0.6215*t - 11.37 * v**0.16 + 0.3965 * t * v**0.16

    return indice


if __name__ == "__main__":
    temperatura = 35
    velocidad = 120
    resultado = indice_temperatura_sensacion(temperatura, velocidad)
    print(f'La temperatura de sensación es igual {resultado}°C.')

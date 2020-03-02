# Ejercicio 716: Crear una función para convertir un número romano a un número entero.

def romano_a_entero(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    entero = 0

    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            entero += romanos[romano[i]]
        
    return entero

print(romano_a_entero('CXXIII')) # 123

# Prueba de escritorio:
# romano = 'CXXIII'
# entero = 0, 100, 110, 120, 121, 122, 123

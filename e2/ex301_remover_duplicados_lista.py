# Ejercicio 301: Crear función para remover los duplicados de una lista de cadenas.

def remover_duplicados(cadenas):
    """
    Remueve los duplicados de una lista de cadenas.
    """
    no_duplicados = []

    for c in cadenas:
        if c not in no_duplicados:
            no_duplicados.append(c)
    
    return no_duplicados


lenguajes = ['Python', 'Java', 'JavaScript', 'Java', 'Java', 'python', 'C++', 'C', 'C++']

print(lenguajes)

resultado = remover_duplicados(lenguajes)

print(resultado)

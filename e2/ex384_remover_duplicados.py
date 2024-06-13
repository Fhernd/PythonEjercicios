# Ejercicio 384: Remover los elementos duplicados en un diccionario.

def remover_duplicados(objetos):
    resultado = {}

    for k, v in objetos.items():
        if v not in resultado.values():
            resultado[k] = v
    
    return resultado


personas = {
    'id1': {
        'nombre': 'Edward',
        'apellido': 'Ortiz'
    },
    'id2': {
        'nombre': 'Daniela',
        'apellido': 'Ordoñez'
    },
    'id3': {
        'nombre': 'Alexander',
        'apellido': 'Meneses'
    },
    'id4': {
        'nombre': 'Edward',
        'apellido': 'Ortiz'
    },
    'id5': {
        'nombre': 'Daniela',
        'apellido': 'Ordoñez'
    }
}

print(len(personas))
print(personas)

personas_no_duplicados = remover_duplicados(personas)

print()

print(len(personas_no_duplicados))
print(personas_no_duplicados)

# Ejercicio 399: Imprimir el contenido de un diccionario con un ciclo for.

productos = {'id1': {'nombre': 'Teclado', 'precio': 63.9}, 'id2': {'nombre': 'Mouse', 'precio': 25.9}, 'id3': {'nombre': 'Deademas', 'precio': 203.9}, 'id4': {'nombre': 'Monitor', 'precio': 299.9}, 'id5': {'nombre': 'Smartphone', 'precio': 453}}

for p in productos:
    print(p)

    for c in productos[p]:
        print('{}: {}'.format(c, productos[p][c]))
    
    print()

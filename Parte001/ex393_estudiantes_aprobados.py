# Ejercicio 393: Contar la cantidad de estudiantes que pasaron un curso.

estudiantes = [{'id': 1, 'nombre': 'Edward', 'paso': True}, {'id': 2, 'nombre': 'Daniela', 'paso': False}, {'id': 3, 'nombre': 'Alexander', 'paso': True}, {'id': 4, 'nombre': 'Julio', 'paso': False}, {'id': 5, 'nombre': 'Sandra', 'paso': False}]

resultado = sum(e['paso'] for e in estudiantes)

print(resultado)

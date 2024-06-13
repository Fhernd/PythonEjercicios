# Ejercicio 97: Imprimir el listado de variables especiales que usa Python.

# nombres = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))

# print('\n'.join(' '.join(nombres[i:i+8]) for i in range(0, len(nombres), 8)))

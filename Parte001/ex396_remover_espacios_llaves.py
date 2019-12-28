# Ejercicio 396: Remover los caracteres de espacio de las llaves de un diccionario.

productos = {'ca   t1': ['Mouse', 'Teclado', 'Deademas'], 'c  at2': ['RAM', 'Procesador', 'Tarjeta gráfica'], 'ca         t3': ['Smartphone', 'Tablet', 'Portátil']}

print(productos)

resultado = {k.translate({32: None}): v for k, v in productos.items()}

print(resultado)

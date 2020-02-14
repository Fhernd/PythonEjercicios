# Ejercicio 622: A partir de un diccionario con los datos de compra y venta calcular la ganancia.

# {
#   "precio_costo": 30.0,
#   "precio_venta": 42.0,
#   "inventario": 1200
# }

def calcular_ganancia(producto):
    ganancia = producto['precio_venta'] * producto['inventario']
    ganancia -= producto['precio_costo'] * producto['inventario']

    return ganancia

producto = {
  "precio_costo": 30.0,
  "precio_venta": 42.0,
  "inventario": 1200
}

resultado = calcular_ganancia(producto)
print('La ganacia total es: %f' % resultado)

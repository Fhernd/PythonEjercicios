# Ejercicio 859: Encontrar todas las palabras de cinco (5) letras en un texto.

import re

extracto = 'Al abrir luna el todo nube, criaturas y acaba los para me recodos que huevos aire, los la el diana ilesa en cosas los. La y ligeros borrachos signos, arcos con pisotean se las no que mudas es. Vilo huido resonancia nino la larga, hule vuelve de la ceniza vuelve resonancia. Los y diminutas helechos mármol que de de manteles me, arroyo el las yo los muertos donde con la de. Estremecidos desgarrados los la fría. Diana diana la arcos las tierra escaleras llanura que desnudo. Me vengo oh luna tierra osos muerte para de. El lentejas de y el...'

patron = r'\b\w{5}\b'

resultado = re.findall(patron, extracto)

print(len(resultado))
print(resultado)

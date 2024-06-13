# Ejercicio 703: Generar una marca de tiempo (timestamp) en el formato RFC 3339.

from datetime import datetime, timezone

rfc_3339 = datetime.now(timezone.utc).astimezone()

print('Marca de tiempo RFC 3339:', rfc_3339)

# Ejercicio 459: Encontrar las n palabras más recurrentes en un texto con la clase Counter.

from collections import Counter
import re

texto = """
En una tarde extremadamente calurosa de principios de julio, un joven salió de la reducida habitación que tenía alquilada en la callejuela de S*** y, con paso lento e indeciso, se dirigió al puente K***.

Había tenido la suerte de no encontrarse con su patrona en la escalera.

Su cuartucho se hallaba bajo el tejado de un gran edificio de cinco pisos y, más que una habitación, parecía una alacena. En cuanto a la patrona, que le había alquilado el cuarto con servicio y pensión, ocupaba un departamento del piso de abajo; de modo que nuestro joven, cada vez que salía, se veía obligado a pasar por delante de la puerta de la cocina, que daba a la escalera y estaba casi siempre abierta de par en par. En esos momentos experimentaba invariablemente una sensación ingrata de vago temor, que le humillaba y daba a su semblante una expresión sombría. Debía una cantidad considerable a la patrona y por eso temía encontrarse con ella. No es que fuera un cobarde ni un hombre abatido por la vida. Por el contrario, se hallaba desde hacía algún tiempo en un estado de irritación, de tensión incesante, que rayaba en la hipocondría. Se había habituado a vivir tan encerrado en sí mismo, tan aislado, que no sólo temía encontrarse con su patrona, sino que rehuía toda relación con sus semejantes. La pobreza le abrumaba. Sin embargo, últimamente esta miseria había dejado de ser para él un sufrimiento. El joven había renunciado a todas sus ocupaciones diarias, a todo trabajo.

En el fondo, se mofaba de la patrona y de todas las intenciones que pudiera abrigar contra él, pero detenerse en la escalera para oír sandeces y vulgaridades, recriminaciones, quejas, amenazas, y tener que contestar con evasivas, excusas, embustes... No, más valía deslizarse por la escalera como un gato para pasar inadvertido y desaparecer.

Aquella tarde, el temor que experimentaba ante la idea de encontrarse con su acreedora le llenó de asombro cuando se vio en la calle.
"""

palabras = re.findall('\w+', texto)

contador = Counter(palabras)

print(contador.most_common(10))

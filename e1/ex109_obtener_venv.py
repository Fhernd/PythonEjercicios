# Ejercicio 109: Obtener el valor de una variable de entorno.

import os

variable_entorno = 'JAVA_HOME'

print(os.getenv(variable_entorno))

variable_entorno = 'MAVEN_HOME'

print(os.getenv(variable_entorno))

variable_entorno = 'CONDA_HOME'

print(os.getenv(variable_entorno))

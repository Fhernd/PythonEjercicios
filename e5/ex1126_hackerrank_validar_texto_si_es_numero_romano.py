# Ejercicio 1126: HackerRank Validar si un texto representa un número romano.

# You are given a string, and you have to validate whether it's a valid Roman numeral. 
# If it is valid, print True. Otherwise, print False. Try to create a regular expression 
# for a valid Roman numeral.

# Input Format

# A single line of input containing a string of Roman characters.

# Output Format

# Output a single line containing True or False according to the instructions above.

# ...

regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

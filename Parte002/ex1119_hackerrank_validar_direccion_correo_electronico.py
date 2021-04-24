# Ejercicio 1119: HackerRank Validar si una dirección de correo electróno es válida.

# A valid email address meets the following criteria:

# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or 
# more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is , , or  characters in length.
# Given  pairs of names and email addresses as input, print each name and email address pair having a valid email 
# address on a new line.

# ...

import email.utils
import re

def is_valid_email(text):
    pattern = r'^[a-z][a-z0-9\-_\.]+[@][a-z]+[.][a-z]{1,3}$'
    
    return re.search(pattern, text)

if __name__ == '__main__':
    contacts = [input() for _ in range(int(input()))]
    
    for c in contacts:
        result = email.utils.parseaddr(c)
        if is_valid_email(result[1]):
            result = email.utils.formataddr(result)
            print(result)

# Ejercicio 1121: HackerRank Calcular el puntaje de un documento XML contando el número de atributos de los elementos.

# You are given a valid XML document, and you have to print its score. The score is calculated by the sum of 
# the score of each element. For any element, the score is equal to the number of attributes it has.

# Input Format

# The first line contains , the number of lines in the XML document.
# The next  lines follow containing the XML document.

# ...

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    total = 0
    
    for e in node.iter():
        total += len(e.attrib)
    
    return total


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

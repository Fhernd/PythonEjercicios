# Ejercicio 1122: HackerRank Encontrar la profundidad máxima de un documento tipo XML.

# You are given a valid XML document, and you have to print the maximum level of nesting in it.
# Take the depth of the root as 0.

# ...

import xml.etree.ElementTree as etree


maxdepth = 0


def depth(elem, level):
    global maxdepth
    
    if maxdepth == level:
        maxdepth += 1
    
    for c in elem:
        depth(c, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

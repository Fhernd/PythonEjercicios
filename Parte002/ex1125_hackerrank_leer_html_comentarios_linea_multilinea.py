# Ejercicio 1125: HackerRank Leer los comentarios de única línea y multilínea con HTMLParser.

# .handle_comment(data)
# This method is called when a comment is encountered (e.g. <!--comment-->).
# The data argument is the content inside the comment tag:

# ...

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    pass
  
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

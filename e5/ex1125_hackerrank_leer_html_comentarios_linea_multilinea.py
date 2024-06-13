# Ejercicio 1125: HackerRank Leer los comentarios de única línea y multilínea con HTMLParser.

# .handle_comment(data)
# This method is called when a comment is encountered (e.g. <!--comment-->).
# The data argument is the content inside the comment tag:

# ...

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data):
            if '\n' in data:
                print(">>> Multi-line Comment")
            else:
                print(">>> Single-line Comment")
            
            print(data)
    def handle_data(self, data):
        if len(data.strip()):
            print(">>> Data")
            print(data)


if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
        
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

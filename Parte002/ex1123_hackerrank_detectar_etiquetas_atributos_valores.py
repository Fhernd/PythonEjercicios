# Ejercicio 1123: HackerRank Extraer las etiquetas, atributos y valores de un documento HTML.

# You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.

# Print the detected items in the following format:

# ...

from html.parser import HTMLParser


class CustomerHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        
        for a, v in attrs:
            print(f'-> {a} > {v}')

if __name__ == '__main__':
    n = int(input())
    
    html = ''
    
    for _ in range(n):
        html += input()
    
    parser = CustomerHtmlParser()
    parser.feed(html)

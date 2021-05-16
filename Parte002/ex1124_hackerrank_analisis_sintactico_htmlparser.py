# Ejercicio 1124: HackerRank Realizar análisis sintáctico a un documento HTML con HTMLParser.

# HTML
# Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

# Parsing
# Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into 
# its component parts and describing their syntactic roles.

# HTMLParser
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, 
# and other markup elements are encountered.

# ...

from html.parser import HTMLParser


class CustomHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print( "Start :", tag)
        
        for a, v in attrs:
            print(f'-> {a} > {v}')
        
    def handle_endtag(self, tag):
        print( "End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print( "Empty :", tag)
        
        for a, v in attrs:
            print(f'-> {a} > {v}')

        
if __name__ == '__main__':
    n = int(input())
    html = ''.join([input() for _ in range(n)])
    
    parser = CustomHtmlParser()
    parser.feed(html)

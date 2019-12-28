# Ejercicio 159: Obtener las últimas noticias desde Google News con Beautiful Soup.

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# Conexión:
url_google_news = 'https://news.google.com/news/rss'
cliente = urlopen(url_google_news)
contenido_xml = cliente.read()
cliente.close()

# Lectura en el formato XML:
pagina = soup(contenido_xml, 'xml')
items = pagina.findAll('item')

# Iterar cada noticia:
for item in items:
    print(item.title.text)
    print(item.link.text)
    print(item.pubDate.text)

    print('=' * 70)

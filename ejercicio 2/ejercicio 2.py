import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://rpp.pe/blog'

# Establece un User-Agent en la solicitud para simular un navegador web
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Realiza una solicitud HTTP al sitio web con los encabezados personalizados
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra los elementos <article> que contienen titulares y autores
    articles = soup.find_all('article', class_='news news-border')

    # Inicializa listas para titulares y autores
    titulares = []
    autores = []

    # Itera sobre los elementos <article>
    for article in articles:
        # Extrae el titular del enlace dentro de h2.news__title
        titular = article.select_one('h2.news__title a')
        titulares.append(titular.text.strip() if titular else 'No titular disponible')

        # Extrae el autor del enlace dentro de span.news__author
        autor = article.select_one('span.news__author a')
        autores.append(autor.text.strip() if autor else 'No autor disponible')

    # Imprime la longitud de las listas
    print('Longitud de titulares:', len(titulares))
    print('Longitud de autores:', len(autores))

    # Imprime algunos ejemplos de titulares y autores
    print('Ejemplo de titulares:', titulares[:5])
    print('Ejemplo de autores:', autores[:5])

    # Verifica si las listas tienen la misma longitud
    if len(titulares) == len(autores):
        # Crea un DataFrame de pandas para almacenar los datos
        data = {'Titular': titulares, 'Autor': autores}
        df = pd.DataFrame(data)

        # Guarda el DataFrame en un archivo Excel
        df.to_excel('datos_blog_rpp.xlsx', index=False)
        print('Datos guardados en datos_blog_rpp.xlsx')
    else:
        print('Las listas no tienen la misma longitud. Revisa los selectores.')
else:
    print('Error al realizar la solicitud:', response.status_code)

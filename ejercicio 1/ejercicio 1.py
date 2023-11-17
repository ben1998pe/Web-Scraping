import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del sitio web que deseas hacer scraping
url = 'https://saway.com.pe/'

# Establece un User-Agent en la solicitud para simular un navegador web
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Realiza una solicitud HTTP al sitio web con los encabezados personalizados
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra elementos en la página web utilizando selectores de CSS
    # En este ejemplo, estamos extrayendo todos los enlaces (<a>) en la página
    enlaces = soup.select('a')

    # Crea un DataFrame de pandas para almacenar los datos
    data = {'Texto del enlace': [enlace.text for enlace in enlaces],
            'URL del enlace': [enlace['href'] for enlace in enlaces]}
    df = pd.DataFrame(data)

    # Guarda el DataFrame en un archivo Excel
    df.to_excel('datos_scraping.xlsx', index=False)
    print('Datos guardados en datos_scraping.xlsx')
else:
    print('Error al realizar la solicitud:', response.status_code)

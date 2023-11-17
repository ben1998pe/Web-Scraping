import requests
from bs4 import BeautifulSoup

# URL del sitio web
url = "https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias"

# Número de RUC a consultar
ruc = "20370146994"

# Parámetros del formulario
params = {
    'nroRuc': ruc,
    'accion': 'consPorRuc',
    'numRnd': '-1500521606',  # Este valor puede cambiar en cada solicitud
}

# Realizar la solicitud POST al formulario
response = requests.post(url, data=params)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar la respuesta HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Aquí puedes buscar y extraer la información que necesitas del objeto 'soup'
    # por ejemplo, puedes encontrar elementos por etiquetas, clases, id, etc.

    # Imprimir el título de la página como ejemplo
    print(soup.title.text)
else:
    print("Error al realizar la solicitud:", response.status_code)

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.bvl.com.pe/rex/aenza"

# Configuración de Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo sin cabeza (sin interfaz gráfica)

# Inicializar el navegador
driver = webdriver.Chrome(options=options)
driver.get(url)

# Esperar a que la página se cargue completamente (puedes ajustar este tiempo según sea necesario)
driver.implicitly_wait(10)

# Obtener el HTML de la página después de que se haya cargado dinámicamente
page_source = driver.page_source

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Encontrar la tabla por su clase
tabla = soup.find('table', {'class': 'table table-dark'})

# Verificar si se encontró la tabla
if tabla:
    # Imprimir el HTML de la tabla
    print(tabla.prettify())
else:
    print("No se encontró la tabla con la clase especificada.")

# Cerrar el navegador
driver.quit()

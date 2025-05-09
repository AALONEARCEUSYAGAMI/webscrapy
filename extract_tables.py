import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del artículo
url = 'https://en.wikipedia.org/wiki/History_of_Python'

# Obtener HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Contenedor principal del contenido
content_div = soup.find('div', {'class': 'mw-parser-output'})

# Buscar encabezados y párrafos de forma recursiva
elements = content_div.find_all(['h1', 'h2', 'h3', 'h4', 'p'], recursive=True)

# Acumular texto limpio
output = []

for elem in elements:
    text = elem.get_text(strip=True)
    if text:
        output.append(text)

# Crear DataFrame
df = pd.DataFrame(output, columns=['Contenido'])

# Guardar en archivo Excel
df.to_excel('contenido_extraido_web.xlsx', index=False)

print("✅ Texto extraído y guardado en 'contenido_extraido_web.xlsx'")

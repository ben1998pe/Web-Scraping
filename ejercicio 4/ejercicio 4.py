
#!apt-get install ocrmypdf -q

#!pip install pdfplumber -q

import os
import csv
import requests
import pdfplumber
from bs4 import BeautifulSoup

#url='https://www.transparencia.gob.pe/personal/pte_transparencia_declaraciones.aspx?id_entidad=145&Ver=&pag=17'
URL_BASE = 'https://www.transparencia.gob.pe'

for n in range(1, 18):
	url = f'https://www.transparencia.gob.pe/personal/pte_transparencia_declaraciones.aspx?id_entidad=145&Ver=&pag={n}'
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')
	tables = soup.find("table", class_='table')
	#links = tables.findAll('a')
	link_text = []
	for a in tables.find_all('a', href=True): 
	    if a.text: 
	        link_text.append(a['href'].replace('../..', URL_BASE))
	print(link_text)
    
    
#funcion descargar
def download_file(url):
    local_filename = url.split('/')[-1]
    
    with requests.get(url) as r:
        assert r.status_code == 200, f'error, status code is {r.status_code}'
        with open(local_filename, 'wb') as f:
            f.write(r.content)
        
    return local_filename

#descarga el archivo
invoice = 'https://www.transparencia.gob.pe/Documentos/Declaraciones/145/Del%20Carpio%20Flores%20Alexandra%20Lizette%20Peri%C3%B3dica%202019.pdf'
invoice_pdf = download_file(invoice)

invoice_pdf

#pasa el archivo a lectura
with pdfplumber.open(invoice_pdf) as pdf:
    page = pdf.pages[0]
    text1 = page.extract_text()
    
    
if text1 == 'None':
        os.system(f'ocrmypdf {invoice_pdf} output.pdf')

        with pdfplumber.open('output.pdf') as pdf:
          page = pdf.pages[0]
          text = page.extract_text(x_tolerance=2)
    #print(text)

          lines = text.split('\n')

          lines

          entidad_entidad = []
          entidad_direccion = []
          entidad_ejerpre = []
          decla_dni = []
          decla_apepa = []
          decla_apema = []
          nombre = []
          oport_ini = []
          oport_ent = []
          oport_cesar = []
          ing_men = []
          bienes = []
          otros = []
          total_fina = []
          lif=[]

          for ln in lines:
            if ln.startswith("ENTIDAD"):
              entidad_entidad.append(ln[7:])
          for ln in lines:
            if ln.startswith("DIRECCION"):
             entidad_direccion.append(ln[9:])
          for ln in lines:
            if ln.startswith("EJERCICIO  PRESUPUESTAL"):
             entidad_ejerpre.append(ln[23:])            
          for ln in lines:
            if ln.startswith("DNVCE"):
             decla_dni.append(ln[5:])
          for ln in lines:
            if ln.startswith("APELLIDO  PATERNO"):
             decla_apepa.append(ln[17:])
          for ln in lines:
            if ln.startswith("APELLIDO  MATERNO "):
             decla_apema.append(ln[18:])
          for ln in lines:
            if ln.startswith("NOMBRES"):
             nombre.append(ln[7:])
          for ln in lines:
            if ln.startswith("AL INICIO"):
             oport_ini.append(ln[9:])
          for ln in lines:
            if ln.startswith("ENTREGA  PERIODICA"):
             oport_ent.append(ln[18:])
          for ln in lines:
            if ln.startswith("AL  CESAR "):
             oport_cesar.append(ln[10:])
          for ln in lines:
            if ln.startswith(" INGRESOS  MENSUALES  *"):
             ing_men.append(ln[23:])
          for ln in lines:
            if ln.startswith("    BIENES  **"):
             bienes.append(ln[14:])
          for ln in lines:
            if ln.startswith(" OTROS  ***"):
             otros.append(ln[11:])
#last_line = lines.readlines()[-1]
#print(last_line)
          headers=['ENTIDAD','DIRECCION','EJERCICIO PRESUPUESTAL','DNI','APELLIDO PATERNO','APELLIDO MATERNO','NOMBRES','AL INICIO','ENTREGA PERIODICA','AL CESAR','INGRESOS MENSUALES','BIENES',' OTROS','TOTAL FINA']
          valuec= entidad_entidad,entidad_direccion,entidad_ejerpre,decla_dni,decla_apepa,decla_apema,nombre,oport_ini,oport_ent,oport_cesar,ing_men,bienes,otros,lif
  
     
          with open('WS05.csv','w+',newline='') as fp:
           a=csv.writer(fp)
           data=valuec
           a.writerow(headers)
           a.writerow(valuec)
else:
    lines2 = text1.split('\n')
    lines2
    entidad_entidad = []
    entidad_direccion = []
    entidad_ejerpre = []
    decla_dni = []
    decla_apepa = []
    decla_apema = []
    nombre = []
    oport_ini = []
    oport_ent = []
    oport_cesar = []
    ing_men = []
    bienes = []
    otros = []
    total_fina = []
    lif=[]

    for ln in lines2:
        if ln.startswith("ENTIDAD"):
         entidad_entidad.append(ln[7:])
    for ln in lines2:
        if ln.startswith("DIRECCIÓN"):
         entidad_direccion.append(ln[9:])
    for ln in lines2:
        if ln.startswith("EJERCICIO PRESUPUESTAL"):
         entidad_ejerpre.append(ln[22:])            
    for ln in lines2:
        if ln.startswith("DNI/CE"):
         decla_dni.append(ln[6:])
    for ln in lines2:
        if ln.startswith("APELLIDO PATERNO"):
         decla_apepa.append(ln[16:])
    for ln in lines2:
        if ln.startswith("APELLIDO MATERNO"):
         decla_apema.append(ln[16:])
    for ln in lines2:
        if ln.startswith("NOMBRES"):
         nombre.append(ln[7:])
    for ln in lines2:
        if ln.startswith("AL INICIO"):
         oport_ini.append(ln[9:])
    for ln in lines2:
        if ln.startswith("ENTREGA PERIÓDICA"):
         oport_ent.append(ln[17:])
    for ln in lines2:
        if ln.startswith("AL CESAR"):
         oport_cesar.append(ln[8:])
    for ln in lines2:
        if ln.startswith("INGRESOS MENSUALES * "):
         ing_men.append(ln[21:])
    for ln in lines2:
        if ln.startswith("BIENES ** "):
          bienes.append(ln[10:])
    for ln in lines2:
        if ln.startswith("OTROS ***"):
          otros.append(ln[9:])
    headers=['ENTIDAD','DIRECCION','EJERCICIO PRESUPUESTAL','DNI','APELLIDO PATERNO','APELLIDO MATERNO','NOMBRES','AL INICIO','ENTREGA PERIODICA','AL CESAR','INGRESOS MENSUALES','BIENES',' OTROS','TOTAL FINA']
    valuec= entidad_entidad,entidad_direccion,entidad_ejerpre,decla_dni,decla_apepa,decla_apema,nombre,oport_ini,oport_ent,oport_cesar,ing_men,bienes,otros,lif      
    with open('WS05.csv','w+',newline='') as fp:
           a=csv.writer(fp)
           data=valuec
           a.writerow(headers)
           a.writerow(data)
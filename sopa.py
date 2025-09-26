# Importar bibliotecas
import requests
from bs4 import BeautifulSoup

def buscar():
    site = "http://www.pfi.uem.br/ingresso/processo-seletivo-doutorado/"
    page = requests.get(site)
    soup = BeautifulSoup(page.text, 'html.parser')
    titulos_class = 'title-heading-left'
    dados = []
    for item in soup.find_all(class_=titulos_class):
        dados.append(item.get_text())
    return dados

def edital_25():
    lista_atual = ['Edital 2/2025', 'Convocações 2/2025', 'Cronograma 2/2025']
    lista = buscar()
    lista25 = []
    for i in lista:
        if "2025" in i or "2026" in i:
            if i not in lista_atual:
                lista25.append(i)
    return lista25, lista

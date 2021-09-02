# PROGRAMA DE ANÁLISE - WEB SCRAPING #
from bs4 import BeautifulSoup
import requests


#Objeto site recebe o conteudo da requisicao http:
site = requests.get('https://www.climatempo.com.br/').content

#Objeto soup baixa o html do site:
soup = BeautifulSoup(site, 'html.parser')

#Transforma o html em string
print(soup.prettify())

#Mostrar uma parte do html específico:
temperatura = soup.find("h4", class_="-gray-dark-2 -normal -font-base")
print(temperatura.string)

#Mostrar o primeiro título que ele acha no html:
print(soup.title.string)

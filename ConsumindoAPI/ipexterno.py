import json
from urllib.request import urlopen


url = 'https://ipinfo.io/json'

urlaberta = urlopen(url)

dados = json.load(urlaberta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

lista = [ip, org, city, region, country]

for n in lista:
    print(n)

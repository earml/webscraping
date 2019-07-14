## Coletando um valor específico em uma página web
import urllib.request
pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html')
texto=pagina.read().decode('utf8')
onde=texto.find('>$') # pego os strongs com >$
inicio = onde + 2 # Aqui eu pulo 2 posições, pois eu não quero nem o '>' e nem o '$'
fim = inicio + 4 #Aqui eu pego o início + 4 (que dá os 2 valores antes da vírgula + os 2 valores depois da             #vírgula)

preco=texto[inicio:fim]
print (preco)


## Coletando um valor específico em uma página web
import urllib.request
pagina = urllib.request.urlopen('http://sinda.crn2.inpe.br/PCD/SITE/novo/site/historico/passo2.php')
texto=pagina.read().decode('utf8')
onde=texto.find('>$') # pego os strongs com >$
inicio = onde + 2 # Aqui eu pulo 2 posições, pois eu não quero nem o '>' e nem o '$'
fim = inicio + 4 #Aqui eu pego o início + 4 (que dá os 2 valores antes da vírgula + os 2 valores depois da             #vírgula)

preco=texto[inicio:fim]
print (preco)

request = urllib.request.Request("http://sinda.crn2.inpe.br/PCD/SITE/novo/site/historico/passo2.php")
response = urllib.request.urlopen(request)
the_page = response.read()
theText = the_page.decode()
text = the_page.decode()
dataCrop = findall("<span>[0-9]+&deg;</span>", text)
print("The data cropped out of the webpage is:", dataCrop)



#Find the printed data...
helloAt = pageStr.find("Hello")
print("Hello at:", helloAt )
print(pageStr[helloAt:helloAt+300] )




## Coletando um valor específico em uma página web que seja menor que determinado valor
import urllib.request
pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html')
texto=pagina.read().decode('utf8')
onde=texto.find('>$') # pego os strongs com >$
inicio = onde + 2 # Aqui eu pulo 2 posições, pois eu não quero nem o '>' e nem o '$'
fim = inicio + 4 #Aqui eu pego o início + 4 (que dá os 2 valores antes da vírgula + os 2 valores depois da             #vírgula)
preco=float(texto[inicio:fim]) # tenho que converter para float, pois o valor coletado estar como string

if  preco <4.74 :
    print (preco)

# Loop para fazer o algoritmo ir a página várias vezes até encontrar o valor desejado

import urllib.request
preco=5.00
while preco >= 4.74:
    pagina = urllib.request.urlopen(
            'http://beans.itcarlow.ie/prices-loyalty.html')
    texto=pagina.read().decode('utf8')
    onde=texto.find('>$') # pego os strongs com >$
    inicio = onde + 2 # Aqui eu pulo 2 posições, pois eu não quero nem o '>' e nem o '$'
    fim = inicio + 4 # Aqui eu pego o início + 4 (que dá os 2 valores antes da vírgula + os 2 valores depois da             #vírgula)
    preco=float(texto[inicio:fim])
print (preco)


# =============================================================================
# Scraper de dados do SIDRA
# =============================================================================
# curso python 1: exemplo de análise de dados em python - youtube
import pandas as pd
from pandas import *
from seaborn import *
from matplotlib.pyplot import *
import numpy as np
from statsmodels.formula.api import *
#matplotlib inline

pd.options.display.max_columns = None
pd.options.display.max_seq_items = None
np.set_printoptions(threshold=np.inf)

import requests
r = requests.get('http://api.sidra.ibge.gov.br/values/t/261/n1/all/n2/all/n3/all/v/all/p/all/c1/all/c2/all/c58/0/d/v93%200,v1000093%202')
df = pd.DataFrame(r.json())
df.to_csv('sidra.texto.csv')   #3
df.head(10)
df.columns = df.iloc[0,:];df.drop(0,inplace=True)



## Coletando um valor específico em uma página web
import urllib.request
pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
texto=pagina.read().decode('utf8')
onde=texto.find('>$') # pego os strongs com >$
inicio = onde + 2 # Aqui eu pulo 2 posições, pois eu não quero nem o '>' e nem o '$'
fim = inicio + 4 #Aqui eu pego o início + 4 (que dá os 2 valores antes da vírgula + os 2 valores depois da             #vírgula)

preco=texto[inicio:fim]
print (preco)

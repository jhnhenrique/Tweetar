import oauth2
import json
import urllib.parse


consumer_key = 'Coloque sua consumer key aqui.'
consumer_secret = 'Coloque o consumer secret aqui.'

token_key = 'Coloque sua token key aqui.'
token_secret = 'Coloque seu token secret aqui.'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Novo tweet: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

print(objeto)
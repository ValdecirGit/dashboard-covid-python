# modulo do python usado para fazer leitura  e manipulação de dados json
import json

#importando arquivo json da localizacao dos estados do brasil utilizando somente o método de leitura opcao 'r'
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

#verificando type da dados
print(type(brazil_states))

#se for dict (dicionario), verificar quais as chaves possui
print((brazil_states.keys()))

#verifico o que tem dentro das chaves
print((brazil_states["type"]))
print((brazil_states["features"]))

#verifico o que o tipo da chave features
print((type(brazil_states["features"])))

#verifico type da chave features - List
print((type(brazil_states["features"])))

#Como é uma lista verifico primeiro elemento da chave 'features'
print((brazil_states["features"][0]))

#verifico o tipo de elemento que é 'dict'
print((type(brazil_states["features"][0])))
#identifico que tenho uma lista de dicionarios ...
#pergunto quais são as chaves desses elementos q sao dicionarios
print((brazil_states["features"][0].keys()))

#indetifico campo principal da lista
print((brazil_states["features"][0]["id"]))
print((brazil_states["features"][0]["geometry"]))
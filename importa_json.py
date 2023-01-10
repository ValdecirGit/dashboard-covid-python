# modulo do python usado para fazer leitura  e manipulação de dados json
import json
#importando arquivo json da localizacao dos estados do brasil utilizando somente o método de leitura opcao 'r'
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))
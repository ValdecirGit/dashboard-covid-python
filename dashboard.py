#bliblioteca responsável pelo gerenciamento do dashboard (servidor, leiaute)
import dash
#dash core components responsável por criar todos os componentes para o dashboard
from dash import dcc
#dash html components, permite colocar códigos html dentro do dashboard 
from dash import html
#dentro do dash acessa as dependencias para pegar o o input e output para criar a interativade com o dashboard
from dash.dependencies import Input, Output
#importa bliblioteca do dash bootstrap para estilizar o dashboard
import dash_bootstrap_components as dbc
#bliblioteca plotly para criação de gráficos com o modulo express utilizando 
# funcoes de alto nivel de forma simples
import plotly.express as px
#biblioteca para outros gráficos
import plotly.graph_objects as go
#biblioteca para trabalhar com computação numérica. Seu principal objeto 
# é o vetor n-dimensional, ou ndarray
import numpy as np
#biblioteca para análise de dados, construção de estrutura, manipulação e 
#limpeza de dados, sendo também utilizada com bibliotecas de processamento 
# numérico e construção de gráficos
import pandas as pd
# modulo do python usado para fazer leitura  e manipulação de dados json
import json

#importo dados especificos dos estados
df_states = pd.read_csv("df_states.csv")
#importo dados especificos dos Brasil
df_brasil = pd.read_csv("df_brasil.csv")

#importando arquivo json da localizacao dos estados do brasil utilizando somente o método de leitura opcao 'r'
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

#-------------------------------------------------------------------------------------------------------------------
#Criação Mapa
#instancia da classe onde vai conter o dashboard, dash modulo instancia a classe 'Dash'


# __name__, parametro basico
# external_stylesheets, para utilizar uma folha de estilo externa
# dbc dash bootstrap componentes, componentes para leiaute
#themes estiliza com temas mais bonitos
# CYBORG tipo de tema escuro
#nos temas podemos usar streams que estão localizadas no endereço www.bootshwatch.comm para ver estilos que podemos usar
# ou na propria bibliteca do bootstrap 'https://dash-bootstrap-components.opensource.faculty.ai/', parte documentação acessa opcao Themes
# a folha de estilo feita externa faz algumas alteracoes no tema CYBORG para ficar mais bonito
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

#filtro um dia a priore, por enqto fixo
df_states_ = df_states[df_states["data"] == "2020-05-13"]

# teste listar filtro do dia priore 
print(df_states_)

#-----------------------------------------------------------------------
#figure elemento que vai conter o mapa

#choropleth_mapbox, mapas onde tem as divisoes coloridos para especificar informações (informações relacao ao covid)
#mapbox opcao para criar graficos visualmente mais bonitos
#df_states, passo primeiro parametro o data frame que possuem os dados q vou usar
#segundo parametro com a coluna onde tera o 'ID' que vai casar com o campo do mapa (geojson)
#terceiro parametros pinta a coluna cfe a coluna de casosNovos
#quarto parametro passo o arquivo geojson que ele vai fazer a referencia
#quinto parametro passo uma paleta de cores 
#sexto parametro passo a opacidade 
#e por ultimo aplico o hover_data que é um dicionario com informações que quero q apresente
#quando eu colocar o cursor em cima do estado, True ou False é se eu quero ou não mostrar
#parametro center é onde eu quero deixar centrado inicialmente o mapa

fig = px.choropleth_mapbox(df_states_, locations="estado", color="casosNovos", 
                           center={"lat": -16.95, "lon": -47.78}, 
                           geojson=brazil_states, color_continuous_scale="Redor", opacity=0.4,
                           hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True})

#================================================                           
# Criando Estilo do layout da figura
fig.update_layout(
    mapbox_style="carto-darkmatter"
)


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
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])

#filtro um dia a priore, por enqto fixo
df_states_ = df_states[df_states["data"] == "2020-05-13"]

#-----------------------------------------------------------------------
#figure elemento que vai conter o mapa
fig = px.choropleth_mapbox(df_states_, locations="estado", color="casosNovos", 
                           center={"lat": -16.95, "lon": -47.78}, 
                           geojson=brazil_states, color_continuous_scale="Redor", opacity=0.4,
                           hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True})

#================================================                           
# Criando Estilo do layout da figura
fig.update_layout(
    mapbox_style="carto-darkmatter"
)

#================================================                           
# Construção do layout
# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
app.layout = dbc.Container (
     #criando linha
     dbc.Row([
        #crio uma coluna
        dbc.Col([
            #componente do Dash responsável por guardar gráficos
            dcc.Graph(id="choropleth-map", figure=fig)
        ]) #fim dbc.Col
     ]) # fim dbc.Row   
) # fim app.layout = dbc.Container

if __name__ == "__main__":
    app.run_server(debug=True)


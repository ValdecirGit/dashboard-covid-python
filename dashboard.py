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

#---------------------------------------------------------------------------------------------------
#Estudo e Manipulação de dados, filtros, extrações do arquivo csv, tipos de dados, 
#conhecimento das informações que serão usadas para os gráficos no dashboard

#import manipula_dados

#importo dados especificos dos estados
df_states = pd.read_csv("df_states.csv")
#importo dados especificos dos Brasil
df_brasil = pd.read_csv("df_brasil.csv")








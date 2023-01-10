#biblioteca para análise de dados, construção de estrutura, manipulação e 
#limpeza de dados, sendo também utilizada com bibliotecas de processamento 
# numérico e construção de gráficos
import pandas as pd
#---------------------------------------------------------------------------------------------------
#Estudo e Manipulação de dados, filtros, extrações do arquivo csv, tipos de dados, 
#conhecimento das informações que serão usadas para os gráficos no dashboard

#importo todos os dados contidos em coluna da planilha para um data frame fazendo a marcação de separação por ponto e vírgula
# o arquivo HIST_PAINEL_COVIDBR_13mai2021.csv será deletado pois os dados foram extraídos para df_states.csv e df_brasil.csv
df = pd.read_csv("HIST_PAINEL_COVIDBR_13mai2021.csv", sep=';')

#filtro todos os estados que não estão em branco e os municipios que estão em branco
df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
print(df_states)

#filtro todas os dados da coluna regiao que for igual a Brasil
df_brasil = df[df["regiao"] == "Brasil"]
print(df_brasil)

#crio os dados filtros para novos arquivo, e comento o arquivo.csv com todos os registros 
df_states.to_csv("df_states.csv")
df_brasil.to_csv("df_brasil.csv")


# -*- coding: utf-8 -*-
"""arvore-sintomas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fUzyvvpURXcMjPhMXENIyb5oCMlUq0O8
"""

import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics

dataset = pd.read_csv('dados26abril22.csv',sep=';')
nomes_classes = ['Recuperação','Risco de óbito']


sexo = list(set(dataset['SEXO'])) 
faixas_etarias = list(set(dataset['FAIXAETARIA']))
hospitalizado = list(set(dataset['HOSPITALIZADO'])) 
febre = list(set(dataset['FEBRE'])) 
tosse = list(set(dataset['TOSSE']))
garganta = list(set(dataset['GARGANTA'])) 
gestante = list(set(dataset['GESTANTE'])) 

encoder = OrdinalEncoder()

dataset['SEXO'] = encoder.fit_transform(pd.DataFrame(dataset['SEXO']))
dataset['FAIXAETARIA'] = encoder.fit_transform(pd.DataFrame(dataset['FAIXAETARIA']))
dataset['EVOLUCAO'] = encoder.fit_transform(pd.DataFrame(dataset['EVOLUCAO']))
dataset['HOSPITALIZADO'] = encoder.fit_transform(pd.DataFrame(dataset['HOSPITALIZADO']))
dataset['FEBRE'] = encoder.fit_transform(pd.DataFrame(dataset['FEBRE']))
dataset['TOSSE'] = encoder.fit_transform(pd.DataFrame(dataset['TOSSE']))
dataset['GARGANTA'] = encoder.fit_transform(pd.DataFrame(dataset['GARGANTA']))
dataset['DISPNEIA'] = encoder.fit_transform(pd.DataFrame(dataset['DISPNEIA']))
dataset['GESTANTE'] = encoder.fit_transform(pd.DataFrame(dataset['GESTANTE']))
dataset['RACA_COR'] = encoder.fit_transform(pd.DataFrame(dataset['RACA_COR']))
dataset['SRAG'] = encoder.fit_transform(pd.DataFrame(dataset['SRAG']))


colunas = dataset.columns.to_list()
nomesColunas = colunas [1:3]
nomesColunas = nomesColunas + colunas [4:8]
nomesColunas = nomesColunas+colunas[9:10]

dataset_features = dataset[nomesColunas]
dataset_classes = dataset['EVOLUCAO']

#divisão dos dados entre treino e teste

feature_treino,feature_teste,classes_treino,classes_teste = train_test_split(dataset_features,
                                                                             dataset_classes,
                                                                             test_size=0.15,
                                                                             random_state=15)

#construção da árvore
arvore = DecisionTreeClassifier()

#treino a arvore
arvore.fit(feature_treino,classes_treino)

#entrada de dados
import streamlit as st

with open("style.css") as f:
	st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.title('Modelo de Predição de Evolução da COVID-19 em pacientes')
st.subheader('Esse projeto utiliza o modelo de árvore de decisão para estudo da base de dados de casos confirmados para COVID-19 da Secretaria de Saúde do RS')
st.write('Projeto vinculado à Universidade Franciscana | Pós-graduação em Nanociências | CAPES')

info_sexo = st.selectbox('Escolha o sexo do paciente', sexo)
info_idade = st.selectbox('Escolha a idade do paciente', faixas_etarias)
info_hospital = st.selectbox('O paciente foi hospitalizado?', hospitalizado  )
info_febre = st.selectbox('O paciente teve febre?', febre )
info_tosse = st.selectbox('O paciente tem tosse?', tosse )
info_garganta = st.selectbox('O paciente tem dor de garganta?', garganta )
info_gestante = st.selectbox('Trata-se de paciente gestante?', gestante )


individuo = [sexo.index(info_sexo), faixas_etarias.index(info_idade), hospitalizado.index(info_hospital), febre.index(info_febre), tosse.index(info_tosse), garganta.index(info_garganta), gestante.index(info_gestante)]

if st.button('Prever evolução'):
 predicao = arvore.predict([individuo])
 st.write('a predição de evolução para esse paciente é: '+nomes_classes[int(predicao[0])])

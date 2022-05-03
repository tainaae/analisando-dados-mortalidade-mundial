# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:22:09 2022

constituir projeto para portfólio:

tratamento de dados 

@author: taina.esteves
"""

import pandas as pd

#Importa dados
main_df = pd.read_csv(r'annual-number-of-deaths-by-cause.csv')

countries = pd.read_csv(r'countries-regions.csv', sep=';')

#Funções auxiliares
def intersection(lst1, lst2):
    if set(lst1) & set(lst2):
        return list(set(lst1) & set(lst2))
    else:
        return ('Sem correspondência')

def in_common(lst1, lst2):
    if set(lst1) & set(lst2):
        return True
    else:
        return False
  
#-----------------------------------------------------------------------------#
#FUNÇÕES PARA TRATAMENTO DE DADOS

#Cria dicionário a partir de sub-regiões e seus países
#entradas teste: countries, 'Sub-region Name','Country or Area', 'ISO-alpha3 Code'
def dict_subregiao_paises(df, subregiao, codigo):
    correspondencias_paises = df.dropna(subset=[codigo])
    
    dict_correspondencias_paises = correspondencias_paises.groupby(subregiao)[codigo].apply(set).to_dict()
    return dict_correspondencias_paises

#seleciona dados comuns apenas aos dois dados
def select_dados_comuns(df1, coluna_df1, df2, coluna_df2):
    lista1 = df1[coluna_df1].dropna().unique().astype(list)
    lista2 = df2[coluna_df2].dropna().unique().astype(list)
    
    if intersection(lista1, lista2):
        paises_comuns_aos_dfs = intersection(lista1, lista2)
        return paises_comuns_aos_dfs
    else:
        print ("erro select dados comuns")

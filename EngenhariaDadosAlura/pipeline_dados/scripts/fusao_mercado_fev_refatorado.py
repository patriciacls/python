'''Esse código é uma melhoria do "fusao_mercado_fev.py", 
onde uso a classe criada no "processamento_dados.py" para facilita a criação do pipeline.
date: 20241001
author: patriciacls'''

'''
Pipeline desenvolvido baseado em aulas da alura
date: 20241001
author: patriciacls'''
import json
import csv

#chamando classe criada
from processamento_dados import Dados


#indicando local arquivos
path_json='data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#EXTRACT USANDO CLASSE DADOS
dados_empresaA= Dados(path_json, 'json' )
print('Colunas Json')
print(dados_empresaA.nome_colunas)
print(f'Quantidade linhas json: {dados_empresaA.qtd_linhas}')
dados_empresaB= Dados(path_csv, 'csv' )
print('Colunas csv')
print(dados_empresaB.nome_colunas)
print(f'Quantidade linhas csv: {dados_empresaB.qtd_linhas}')

#TRANSFORM
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print('Colunas FUSAO')
print(dados_fusao.nome_colunas)
print('QUANTIDADE LINHAS FUSAO')
print(dados_fusao.qtd_linhas)
dados_empresaB= Dados(path_csv, 'csv' )

#LOAD
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)


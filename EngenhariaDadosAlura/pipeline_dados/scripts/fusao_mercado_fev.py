'''
Pipeline desenvolvido baseado em aulas da alura
date: 20241001
author: patriciacls'''
import json
import csv

#chamando classe criada
from processamento_dados import Dados

# #função p ler aqrv empresa armazenava em json
# def leitura_json(path_json):
#     dados_json = []
#     with open(path_json, 'r') as file:
#         dados_json = json.load(file)
#     return dados_json

# #função p ler aqrv empresa armazenava em csv
# def leitura_csv(path_csv):

#     dados_csv = []
#     with open(path_csv, 'r') as file:
#         spamreader = csv.DictReader(file, delimiter=',')
#         for row in spamreader:
#             dados_csv.append(row)
            
#     return dados_csv

# #função p ler aqrv em função do parametro 
# # tipo de arquivo informado
# def leitura_dados(path, tipo_dado):
#     lendo = []
#     if tipo_dado == "csv" :
#         lendo = leitura_csv(path)
#     elif tipo_dado  == "json":
#         lendo = leitura_json(path)
#     return lendo

# #retornar colunas
# def get_columns(dados):
#     return list(dados[-1].keys())

# def size_data(dados):
#     return len(dados)

# #renomeando colunas, pega dados antigos e coloca no novo
# def rename_columns(dados, key_mapping):
#     new_dados_csv = []

#     for old_dict in dados:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             dict_temp[key_mapping[old_key]] = value
#         new_dados_csv.append(dict_temp)
#     return new_dados_csv

# #juntar dados
# def join(dadosA, dadosB):
#     combined_list= []
#     combined_list.extend(dadosA)
#     combined_list.extend(dadosB)
#     return combined_list

# def transformando_dados_tabela(dados, nomes_colunas):
#     dados_combinados_tabela = [nomes_colunas]

#     for row in dados:
#         linha = []
#     for coluna in nomes_colunas:
#         linha.append(row.get(coluna, 'Indisponivel'))
#     dados_combinados_tabela.append(linha)
#     return dados_combinados_tabela

# def salvando_dados(dados,path):
    # with open(path_dados_combinados,'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(dados)
        
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

# #aplicando a leitura para os arquivos.Lendo nome colunas.
# dados_json = leitura_dados(path_json,'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)
# print (f"nome colunas dados json: {nome_colunas_json}")
# print(f"tamanho dados json: {tamanho_dados_json} .")

# dados_csv = leitura_dados(path_csv,'csv')
# nome_colunas_csv= get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)
# print(nome_colunas_csv)
# print(f"tamanho dados csv: {tamanho_dados_csv} .")
# print(f"total de registros que devera ter com join: {tamanho_dados_csv+tamanho_dados_json}")
# #renomear as colunas

# key_mapping

# #renomeando a tabela definida pela equipe analytics (escolheram manter na csv)
# dados_csv = rename_columns(dados_csv,key_mapping)
# nome_colunas_csv = get_columns(dados_json)
# print(nome_colunas_csv)

# #unir os dados
# dados_fusao = join(dados_json,dados_csv)
# #validar a união
# nome_colunas_fusao= get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(f"colunas fusão: {nome_colunas_fusao}")
# print(f"quantidade registros após o join {tamanho_dados_fusao}")

#salvando dados
#dados_fusao_tabela = transformando_dados_tabela(dados_fusao,nome_colunas_fusao)
#path_dados_combinados = 'data_processed/dados_combinados.csv'

#salvando_dados(dados_fusao_tabela,path_dados_combinados)

#print(path_dados_combinados)

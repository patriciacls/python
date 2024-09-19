import json
import csv

path_json='data_raw/dados_empresaA.json'

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json
    

dados_json = leitura_json(path_json)
print(dados_json[0])


def leitura_csv(path_csv):

    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
            
    return dados_csv
    
dados_json = leitura_json(path_json)
print(path_json[0])

path_json = leitura_json(path_csv)
print(dados_json[0])
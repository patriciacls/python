import json
import csv
#função p ler aqrv empresa armazenava em json
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json
#função p ler aqrv empresa armazenava em csv
def leitura_csv(path_csv):

    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
            
    return dados_csv
#função p ler aqrv em função do parametro tipo de arquivo informado
def leitura_dados(path, tipo_dado):
    lendo = []
    if tipo_dado == "csv" :
        lendo = leitura_csv(path)
    elif tipo_dado  == "json":
        lendo = leitura_json(path)
    return lendo
#indicando local arquivos
path_json='data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
#aplicando a leitura para os arquivos.
dados_json = leitura_dados(path_json,'json')
print(dados_json[0])
dados_csv = leitura_dados(path_csv,'csv')
print(dados_csv[0])

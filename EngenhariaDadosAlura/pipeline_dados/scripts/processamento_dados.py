class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        
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

    #função p ler aqrv em função do parametro 
    # tipo de arquivo informado
    def leitura_dados(path, tipo_dado):
        lendo = []
        if tipo_dado == "csv" :
            lendo = leitura_csv(path)
        elif tipo_dado  == "json":
            lendo = leitura_json(path)
        return lendo
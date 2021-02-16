import requests
import csv

norte = 0
nordeste = 0
sudeste = 0
sul = 0
centro_oeste = 0

request = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')

resultado = request.json()

for estado in resultado:
    regiao = estado['regiao']
    if (regiao['id'] == 1):
        norte += 1
    elif (regiao['id'] == 2):
        nordeste += 1
    elif (regiao['id'] == 3):
        sudeste += 1
    elif (regiao['id'] == 4):
        sul += 1
    elif (regiao['id'] == 5):
        centro_oeste += 1



with open('quant_estados.csv', 'w', newline='') as file:
    writter = csv.writer(file)

    writter.writerow(["Região", '|', "Qtd. Estados"])
    writter.writerow(["Norte", '|', "{}".format(str(norte))])
    writter.writerow(["Nordeste", '|', "{}".format(str(nordeste))])
    writter.writerow(["Sudeste", '|', "{}".format(str(sudeste))])
    writter.writerow(["Sul", '|', "{}".format(str(sul))])
    writter.writerow(["Centro-Oeste", '|', "{}".format(str(centro_oeste))])
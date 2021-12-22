import json
# método para manipular json

# inventario={}   
# se deixar vazio, vai sobrescrever toda hora, vamos abrir o já pronto

import os
def chamarMenu():
    escolha = int(input("Digite: <1> para registrar ativo e <2> para exibir ativos armazenados: "))
    return escolha

# para não dar problema caso o arquivo não exista ainda
def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario=json.load(arq_json)
            # descarrega o arquivo informado em uma variável
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario,arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)
         # método só para json, primeiro paramêtro oq será gravado e segundo onde será gravado

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario,arquivo)
    return "JSON gerado!!!!"

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])
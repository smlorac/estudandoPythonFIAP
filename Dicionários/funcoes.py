def perguntar():
    resposta=input("O que deseja realizar? <I> para inserir usuário, <P> para pesquisar usuário, <E> para excluir um usuário, <L> para listar um usuário. ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Login: ").upper()]=[input("Nome: ").upper(), input("Última data de acesso: "), input("Última estação utilizada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista != None:    #verificar se a lista não está vazia
        print("Nome: " + lista[0])
        print("Último acesso: " + lista[1])
        print("Última estação: " + lista[2])

def deletar(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Usuário excluído")

def listar(dicionario):
    for chave, valor in dicionario.items():   #pesquisa dois valores no foreach e o items retorna em forma de lista os elementos do dicionario
        print("Usuário: ")
        print("Login: ", chave)
        print("Dados: ", valor)

#pode usar o values() retorna só os valores e o keys() só as chaves
#has_key() para verificar se existe aquela chave
#clear() esvazia o dicionario
#popitem() executa elementos de forma aleatória e os exclui
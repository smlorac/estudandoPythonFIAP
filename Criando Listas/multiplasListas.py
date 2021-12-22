equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite S para continuar ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..:  ", (indice+1))
    print("Nome: ", equipamentos[indice])
    print("Valor: ", valores[indice])
    print("Número: ", seriais[indice])
    print("Departamento: ", departamentos[indice])

busca=input("Digite o número do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor: ", valores[indice])

#desafio 1, depreciação das impressoras
for indice in range(0, len(equipamentos)):
    if equipamentos[indice] == "Impressora":
        print("Novo valor: ", (valores[indice]*0.9))

#desafio 2, deletando um equipamento
excluir=int(input("Digite o número do equipamento que será excluído: "))
for indice in range(0, len(equipamentos)):
    if seriais[indice] == excluir:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]
        del departamentos[indice]
        break
print(equipamentos)
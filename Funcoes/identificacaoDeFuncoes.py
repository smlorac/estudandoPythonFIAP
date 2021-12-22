def adicionarItens(inventario):
    resposta = "S"
    while resposta == "S":
        equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
        inventario.append(equipamento)
        resposta = input("Digite S para continuar: ").upper()

def exibirItens(inventario):
    for elemento in inventario:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

def buscarItens(inventario):
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in inventario:
        if busca==elemento[0]:
            print("Valor..: ", elemento[1])
            print("Serial.:", elemento[2])

def depreciarItens(inventario):
    depreciacao=input("Digite o nome do equipamento que será depreciado: ")
    for elemento in inventario:
        if depreciacao==elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * 0.9
            print("Novo valor: ", elemento[1])

def excluirItens(inventario):
    serial=int(input("Digite o serial do equipamento que será excluído: "))
    for elemento in inventario: 
        if elemento[2]==serial:
            inventario.remove(elemento)

def resumoValores(inventario):
    valores=[]
    for elemento in inventario:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O mais caro é ", max(valores))
        print("O mais barato é ", min(valores))
        print("O total é ", sum(valores))
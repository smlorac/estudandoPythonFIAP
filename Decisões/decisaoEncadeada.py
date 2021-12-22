nome=input("Nome: ")
idade=int(input("Idade: "))
doenca=input("Suspeito(a) de doença infecto-contagiosa? ").upper()
if idade >=65:
    print("Paciente COM prioridade")
    if doenca=="SIM":
        print("sala AMARELA")
    elif doenca=="NAO":
        print("sala BRANCA")
    else:
        print("Responda a doença com sim ou nao")
else:
    print("Paciente SEM prioridade")
    if doenca=="SIM":
        print("sala AMARELA")
    elif doenca=="NAO":
        print("sala BRANCA")
    else:
        print("Responda a doença com sim ou nao")
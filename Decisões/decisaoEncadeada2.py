nome=input("Nome: ")
idade=int(input("Idade: "))
doenca=input("Suspeito(a) de doença infecto-contagiosa? ").upper()

# primeiro problema - doença
if doenca=="SIM":
    print("sala AMARELA")
elif doenca=="NAO":
    print("sala BRANCA")
else:
    print("responda com sim ou nao")

# segundo problema - prioridade
if idade >=65:
    print("COM prioridade")
else:
    genero=input("Gênero: ").upper()
    if genero=="F" and idade>10:
        gravidez=input("Grávida: ").upper()
        if gravidez=="SIM":
            print("COM prioridade")
        else:
            print("SEM PRIORIDADE")
    else:
        print("SEM prioridade")
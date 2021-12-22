nome=input("Nome: ")
idade=int(input("Idade: "))
doenca=input("Suspeito(a) de doença infecto-contagiosa? ").upper()
# toUpperCase()
if idade >=65 and doenca=="SIM":
    print(nome + " será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca=="SIM":
    print(nome + " será direcionado para SALA AMARELA - SEM prioridade")
elif idade >=65 and doenca=="NAO":
    print(nome + " será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca=="NAO":
    print(nome + " será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença com sim ou nao")


nome=input("Nome: ")
idade=int(input("Idade: "))
prioridade="NAO"
if idade >=65:
    prioridade="SIM"
print(nome + " possui atendimento prioritário? " + prioridade)
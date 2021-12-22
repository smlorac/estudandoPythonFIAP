inventario=[]
resposta="S"
while resposta=="S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Digite S para continuar! ").upper()
#o append adiciona novos itens na lista

for elemento in inventario:
    print(elemento)
#estrutura forEach
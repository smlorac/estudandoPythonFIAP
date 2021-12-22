numero = int(input("Qual tabuada você quer? "))
print("Tabuada do ", numero)
for multiplicador in range(1, 11, 1):
    multiplicacao = numero*multiplicador
    print(str(numero) + " X " + str(multiplicador) + " = " + str(multiplicacao))

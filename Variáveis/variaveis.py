# string
nome="Caroline Silva"  
empresa="UNILA"
# int
qntFuncionarios = 7
# float
mediaSalario = 3500.25

print(nome + " trabalha na empresa " + empresa)
print("Possui ", qntFuncionarios, " funcionarios.")
print("Média do salário é " + str(mediaSalario))

# o + concatena strings, a virgula diz que acabou o fim da string e o inicio da outra, podendo utilizar int
# por fim pode-se convertar as variaveis numéricas para string

nome=input("Digite seu nome: ")
sobrenome=input("Digite seu sobrenome: ")
idade=int(input("Digite sua idade: "))
altura=float(input("Digite sua altura: "))
print(nome + " " + sobrenome)
print("Tipos de dados: ", type(nome), type(sobrenome))
print(idade, " anos e " + str(altura))
print("Tipos de dados: ", type(idade), type(altura))
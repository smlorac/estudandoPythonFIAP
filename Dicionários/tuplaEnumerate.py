usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Email: ").lower())
    resp=input("Digite s para continuar").upper()
#criamos um dicionario para usuarios e queremos o email como chave, porém esses podem se repetir, logo inserimos eles em uma lista e geramos tuplas formadas por numeros sequenciais e o email

tupla = list(enumerate(emails))
#enumeramos cada item da lista emails e geramos umas tupla formada pelo numero e email
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=input("Nome: "), input("Nível")

for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])
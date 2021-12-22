ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeros octetos: "), input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite s para continuar! ").upper()

print("Exibindo ips")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

print("Exibindo máquinas no mesmo endereço")
pesquisa=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    if (ip[1] ==pesquisa):
        print(nome)

print("Exibindo máquinas na mesma rede")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)
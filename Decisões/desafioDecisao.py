nivel=input("Nível de acesso: ")
# ADM, USR, GUEST
if nivel=="GUEST":
    print("Olá visitante")
elif nivel=="ADM" or nivel=="USR":
    genero=input("Gênero: ")
    # F ou M
    if nivel=="ADM" and genero=="F":
        print("Olá administradora")
    elif nivel=="ADM" and genero=="M":
        print("Olá administrador")
    elif nivel=="USR" and genero=="F":
        print("Olá usuária")
    elif nivel=="USR" and genero=="M":
        print("Olá usuário")
    else:
        print("Digite F ou M para gênero")
else:
    print("Digite ADM, USR ou GUEST")
import socket

resp="S"
while resp=="S":
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP da url é: ", ip)
    resp=input("Digite S para continuar!").upper()
from socket import *

servidor="127.0.0.1" #localhost
porta=43210

obj_socket=socket(AF_INET, SOCK_STREAM)
#criando objeto socket com dois parâmetros: AF_INET (emissor do pacote via DNS ou IP), SOCK_STREM (protocolo TCP) se fosse SOCK_DGRAM (protocolo UDP)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)
#máximo 2 clientes
print("Aguardando cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida=str(conexao.recv(1024)) #pacote de 1024 bytes
        print("Recebemos: ",  str(msg_recebida)[2:-1])
        msg_enviada=bytes(input("Sua resposta: "), 'utf-8')
        #o b é para enviar no formato bytes
        conexao.send(msg_enviada)
        break
    conexao.close()
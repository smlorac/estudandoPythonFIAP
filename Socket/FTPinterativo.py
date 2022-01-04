import os
from ftplib import *

ftp_ativo=False
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
print(ftp.getwelcome())

usuario=input("Usuario: ")
senha=input("Senha: ")
ftp.login(usuario, senha)
print("Conexão bem sucedida.\nDiretório atual de trabalho: ", ftp.pwd())

menu="1"
while menu == "1" or menu == "2" or menu == "3":
    menu=input("Digite 1 para listar arquivos, 2 para definir um diretório e 3 para baixar um arquivo. ")
    if menu == "1":
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("Digite o diretório que deseja: "))
        print("Diretório atual: ", ftp.pwd())
    elif menu == "3":
        tipo=input("Digite B para arquivo binário ou A para arquivo ASCII: ").upper()
        if tipo == "B":
            with open(input("Digite o nome do arquivo destino: ", 'wb')) as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem: "), escreverLinha)
        print("Arquivo baixado!")
ftp.quit()
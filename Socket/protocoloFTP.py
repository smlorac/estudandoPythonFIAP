from ftplib import *

ftp_ativo=False #conexao passiva
ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())

usuario=input("Usuário: ")
senha=input("Senha: ")
ftp.login(usuario, senha)
print("Diretório atual: ", ftp.pwd()) #retorna o endereço atual de trabalho

ftp.cwd('pub')  #andar entre diretórios
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST')) #mostra arquivos

ftp.quit()
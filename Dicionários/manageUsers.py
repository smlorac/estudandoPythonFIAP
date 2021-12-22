from Funções.funcoesDicionarios import *

usuarios={}
opcao=perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
   if opcao=="I":
      inserir(usuarios)
   if opcao=="P":
      pesquisar(usuarios, input("Login? ").upper())
   if opcao=="E":
      deletar(usuarios, input("Login? ").upper())
   if opcao=="L":
      listar(usuarios)
   opcao=perguntar()
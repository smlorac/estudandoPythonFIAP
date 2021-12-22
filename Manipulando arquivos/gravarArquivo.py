with open("teste.txt", "w") as arquivo:
    arquivo.write("Criando meu primeiro arquivo")

# com r é apenas para leitura, w é para sobrescrita, a é para append, x cria um arquivo exclusivo e t retorna como string o conteúdo, diferente do b que retornaria binário

with open("teste.txt", "w") as arquivo:
    arquivo.write("adicionando texto??")
# não adiciona, sobrescreve o outro
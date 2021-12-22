with open("index.html", "w") as pagina:
    pagina.write("<body><h1> Este é um teste para uma página web</h1>")
    pagina.write("<br><h2>Abaixo seguem nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")
    nome=""
    while nome != "SAIR":
        nome = input("Digite seu nome ou SAIR:" ).upper()
        if nome != "SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")
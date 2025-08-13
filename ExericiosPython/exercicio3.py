with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
# substitui
conteudo_modificado = conteudo.replace(" ", "_")
# mostra
print(conteudo_modificado)

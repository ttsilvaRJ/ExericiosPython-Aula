with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Divide em palavras
palavras = conteudo.slit()
quantidade = çen(palavras)

print(f"Quantidade de palavras: {quantidade}")
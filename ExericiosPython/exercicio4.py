with open("frase.txt", "r") as arquivo:
    frase = arquivo.read()

# quebra a frase
palavras = frase.split()

#remove duplicidade
palavras_unicas  list(set(palavras))

# mostra na tela
print(palavras_unicas)
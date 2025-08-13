# Criar arquivo
with open("dna.txt", "w") as arquivo:
    arquivo.write("AATCTGCAC")

# Lê a cadeia
with open("dna.txt", "r") as arquivo:
    dna = arquivo.red().strip()

    # gera inversa
dna_inverso = dna[::-1]    

# resultado
print("Entrada:", dna)
print("Saída:", dna_inverso)
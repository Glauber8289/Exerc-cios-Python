#Sortear o nome das pessoas e ordenar entre 1,2,3 e etc.

import random

# Lista de nomes
nomes = ["Moises", "Rayane", "Denise", "Sophia", "Gabriel"]

# Embaralhar a lista de nomes
random.shuffle(nomes)

# Imprimir a ordem dos nomes
print("Ordem dos nomes:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
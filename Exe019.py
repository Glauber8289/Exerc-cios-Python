#Faça um programa que sorteie o nome de 5 pessoas e escolha 1.

import random

# Lista de nomes
nomes = ["Peçonho", "Maquinhos", "Clara", "Moisés", "Pri","Will","Gabriel"]

# Sortear um nome aleatório
nome_sortiado = random.choice(nomes)

print("O nome sorteado é:", nome_sortiado)

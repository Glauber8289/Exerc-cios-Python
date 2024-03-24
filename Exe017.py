#Faça um programa que leia o comprimento do cateto oposto cateto adjacentee do  de um triangulo retangulo calcule e mostre o valor da hipotenusa .

import math

n=float(input('Digite o valor do cateto oposto'))
n1=float(input('Digite o valor do cateto adjacente'))

h= math.sqrt(math.pow(n,2))+math.sqrt(math.pow(n1,2))


print("O valor da hipotenusa e {}".format(h))
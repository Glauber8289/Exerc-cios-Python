#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse angulo.

import math

n= float(input("Digite o valor do angulo:"))

s= math.sin(math.radians(n))
c= math.cos(math.radians(n))
t=math.tan(math.radians(n))

print('O valor do seno e do cosseno do angulo {} é {:.2f} Seno e {:.2f} Cosseno e {:.2f} Tangente'.format(n,s,c,t))


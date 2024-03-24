#Faça um algoritimo que leia o preço do produto e calcule o preço dele com 5% de desconto

v=float(input('Digite o valor do produto:'))
d=v*0.05

print('O valor do produto e {} mas com o desconto fica {}'.format(v,v-d))
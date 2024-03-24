#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar,sabendo que o carro custa 60R$ por dia e 0.15 por km rodado.


Q=float(input("Quantos km você percorreu ? "))

D=int(input("Qual a quantidade de dias o carro ficou alugado ? "))

Q1= Q*0.15
D1=D*60

V=Q1+D1

print('O Valor total a pagar pelo aluguel do carro é {:.2f}'.format(V))



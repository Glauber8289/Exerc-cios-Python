#Fazer um programa que leia a largura e altura de uma parede em metros.Calcule a sua área e a quantidade necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²


a=(float(input("Digite a Altura:")))
l=(float(input('Digite a largura:')))

area= a*l
t=2

print ("A sua area e de {}m² e voce precisara de {} litros de tinta para pintar essa área".format(area,area/t))


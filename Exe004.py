#Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele.

n = input('Digite algo:')
print (' O tipo primitivo desse valor e',type(n))
print (' Este valor tem espaços? ',n.isspace())
print (' Este valor e um numero ? ',n.isnumeric())
print (' Este valor e alfabetico ? ',n.isalpha())
print (' Este valor e alfanumerico ? ',n.isalnum())
print (' Este valor esta em maisculas ? ',n.isupper())
print (' Este valor esta em minusculas ? ',n.islower())
print (' Este valor esta capitalizado ? ',n.istitle())

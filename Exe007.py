#Desenvolva um programa que leia  2 notas de um aluno e calcule a sua média

n=int(input("Digite uma nota:"))
n1=int(input("Digite outra nota:"))

média=(n+n1)/2

print("A média das notas entre {} e {} é igual a {:.1f}".format(n,n1,média))
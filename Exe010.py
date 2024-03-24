#Fazer um conversor de moedas converter de reias para dolar considerando que 1 real vale 3,27

r=float(input("Quanto você tem na carteira R$ ?"))

d=r/3.27

print("O seu valor em reais é {:.2f} e ele equivale a {:.2f} dolares".format(r,d))
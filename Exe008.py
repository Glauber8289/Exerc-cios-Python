#Programa que diz quantos km,hm,dam,dm,cm,mm vale uma medida em metros digitada 

m=float(input("Digite uma distancia em metros"))

cm=m*100
mm=m*1000
dm=m*10

km=m/1000
hm=m/100
dam=m/10

print("Essa distancia de {} m equivale a {} cm equivale a {} mm equilave a {} dm equivale a {} km equivale a {} hm equivale a {} dam ".format(m,cm,mm,dm,km,hm,dam))
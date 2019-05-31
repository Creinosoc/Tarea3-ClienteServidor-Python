import random

caras = 6
dado1 = []
dado2 = []

intentos = 3

def dado_imprimir(dado,intentos):
	sum=0
	for i in range(intentos):
		print("tiro el dado",i+1,"veces")
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
		print("dado 1 = ",dado)
	print("la suma de sus tiradas es = ",sum)

def dado_calcular(dado,intentos):
	sum=0
	for i in range(intentos):
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
	return sum

print("intentos jugador 1")
# dado_imprimir(dado1,intentos)
j1 = dado_calcular(dado1,intentos)
print("-----------------------------------")
print("intentos jugador 2")
# dado_imprimir(dado2,intentos)
j2 = dado_calcular(dado2,intentos)
print(" ")
print("-----------------------------------")
print ("Jugador 1 saco un total de : ", j1)
print ("Jugador 2 saco un total de : ", j2)

if j1 > j2:
	print("Gano el Jugador 1 con",j1 )
else:
	print("Gano Jugador 2 con",j2 )






#resultado = random.randint(1,6)
#print("El dado giro y obtuvo: ", resultado)

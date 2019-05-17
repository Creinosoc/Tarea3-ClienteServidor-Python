import random

caras = 6
dado1 = []
dado2 = []

intentos = 3

def dado(dado,intentos):
	sum=0
	for i in range(intentos):
		print("tiro el dado",i+1,"veces")
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
		print("dado 1 = ",dado)
	print("la suma de sus tiradas es = ",sum)


print("intentos jugador 1")
dado(dado1,intentos)
print("-----------------------------------")
print("intentos jugador 2")
dado(dado2,intentos)










#resultado = random.randint(1,6)
#print("El dado giro y obtuvo: ", resultado)
	
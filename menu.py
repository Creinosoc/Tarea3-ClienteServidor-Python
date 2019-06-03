import os
import random
import time
 
def menu():
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 Dice War!!!")	
	print ("\t2 - colgado")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")
while True:
	menu()

	opcionMenu = input() #Dice War

	if opcionMenu=="1":
		print("")
		caras = 6
		dado1 = []
		dado2 = []

		print("nombre del jugador")
		nombre = input()

		n_intentos = 100
		print(" se lanzaran  =",n_intentos)

		def dado(dado,intentos):
			sum=0
			for i in range(intentos):
				print("tiro el dado",i+1,"veces")
				dado.append(random.randint(1,caras))
				sum=sum+dado[i]
				print("dado 1 = ",dado)
			print("la suma de sus tiradas es = ",sum)
			return(sum)

		def win(a,b,nombre):
			if a<b:
				print("el ganador es Servidor con la suma de",b)
			else:
				print("el ganador es ",nombre +" con la suma de",a)

		print("intentos ",nombre)
		a=dado(dado1,n_intentos)
		print("-----------------------------------")
		print("intentos servidor")
		b=dado(dado2,n_intentos)


	elif opcionMenu=="2":
		print(" _____________________________________________")
		print("|_____________________________________________|")
		print("|   Bienvenido al juego del quemado :) !!!    |")
		print("|_____________________________________________|")

		print(">> Adivina la palabra antes de morir quemado wajaja!")
		time.sleep(2)
		print(">> Te daré una pista: civilizaciones del famoso Age of Empire II")
		time.sleep(3)
		print("---------------------------------")
		print(">> Empecemos...")

		nombre = input ("¿Como te llamas?"'\n')
		print(" ")
		print ("Hola, "+nombre,"Es hora de jugar al ahorcado AoE 2"'\n')
		print(" ")
		time.sleep(1)
		print("Comienza a adivinar"'\n')
		print(" ")
		time.sleep(0.5)

		lista =['bizantinos','celtas','chinos','francos','godos','ingleses','japoneses','mongoles','turcos','vikingos']

		civilizacion = random.randint(0, len(lista))
		for i in [0,civilizacion]:
			if i== civilizacion:
				palabra = lista[i]
		        #print("la civilizacione es",lista[i])
		tupalabra= ''
		vidas= 5

		while vidas > 0:
		    fallas = 0
		    for letra in palabra:
		        if letra in tupalabra:
		            print(letra,end="")
		        else:
		            print("*", end="")
		            fallas+=1
		    if fallas == 0:
		        print("")
		        print("Felicicades, ganaste"'\n')
		        break
		    tuletra=input('\n'"Introduce una letra: "'\n')
		    tupalabra+=tuletra

		    if tuletra not in palabra:
		        vidas-=1
		        print("Equivocacion"'\n')
		        print("Tu tienes", +vidas, "vidas")

		    if vidas == 0:
		        print("Perdiste!"'\n')
		else:
			print("Gracias por participar"'\n')
	
	elif opcionMenu=="3":

		print ("")

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
import os
import random
import time
 

def menu():

	# Función que limpia la pantalla y muestra nuevamente el menu

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls

	print ("Selecciona una opción")

	print ("\t1 Dice War!!!")

	print ("\t2 - colgado")

	print ("\t3 - tercera opción")

	print ("\t9 - salir")

 

 

while True:

	# Mostramos el menu

	menu()

 

	# solicituamos una opción al usuario

	opcionMenu = input("inserta un numero valor >> ")

 

	if opcionMenu=="1":
		print ("")
		
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

		def win(a,b,nom):
			if a<b:
			print("el ganador es Servidor con la suma de", b)
			else:
			print("el ganador es ",nombre" con la suma de",a)

		print("intentos ",nombre)
		a=dado(dado1,n_intentos)
		print("-----------------------------------")
		print("intentos servidor")
		b=dado(dado2,n_intentos)


	elif opcionMenu=="2":

		print ("")

		input("Colgado!")

		nombre = input ("¿Como te llamas?")
		print(" ")
		print ("Hola, "+nombre,"Es hora de jugar al ahorcado")
		print(" ")
		time.sleep(1)
		print("Comienza a adivinar")
		print(" ")
		time.sleep(0.5)
		palabra ='chile'
		palabra1 ='makako'
		palabra2 ='kkkkk'
		palabra3 ='pip'
		palabra4 ='sacerdotes'
		palabra5 ='titanes'
		palabra6 ='olimpicos'
		palabra7 ='caballeros'
		palabra8 ='faraones'
		palabra9 ='defensores'
		palabra10 ='faeries'
		lista =['chile','makako','kkkkk','pip','sacerdotes','titanes']

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
		        print("Felicicades, ganaste")
		        break
		    
		    tuletra=input("Introduce una letra: ")
		    tupalabra+=tuletra

		    if tuletra not in palabra:
		        vidas-=1
		print("Equivocacion")
		        print("Tu tienes", +vidas, "vidas")

		    if vidas == 0:
		        print("Perdiste!")
		else:
			print("Gracias por participar")


	elif opcionMenu=="3":

		print ("")

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")

	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

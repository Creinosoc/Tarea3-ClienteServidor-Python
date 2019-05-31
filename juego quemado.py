import time
import random

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
nombre = input (">> ¿Como te llamas?"'\n')
print (">> Hola, "+nombre,"empieza probando una letra a la vez...")
time.sleep(2)
print(">> Adivina la palabra!!!"'\n')
time.sleep(1)

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
            print("-", end="")
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

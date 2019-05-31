import time
import random
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

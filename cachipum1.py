import random
from time import sleep

def ganador(tu,pc):
    if pc > tu:
        print ("Gano el PC", pc, "a", tu)
    elif pc == tu:
        print ("Empataron", tu, "a", pc)
    else:
        print ("Ganaste", tu, "a", pc)

 

x = 0
tu = 0
pc = 0

print ("Bienvenido, vamos a jugar a Piedra, papel o tijera.")
sleep(2)
print ("Jugamos!!")
sleep(1)
print ("")

print ("Piedra, papel o tijera?")
opcion = input()
opcion = opcion.lower()
azar = random.choice(["piedra", "papel", "tijera"])
if opcion == azar:
    print ("El pc tambien elijio", azar)
    ganador(tu,pc)
    print ("")
elif azar == "tijera" and opcion == "papel":
    x += 1
    pc += 1
    print ("El PC saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
elif azar == "tijera" and opcion == "piedra":
    x += 1
    tu += 1
    print ("El PC saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
elif azar == "piedra" and opcion == "tijera":
    x += 1
    pc += 1
    print ("El PC saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
elif azar == "piedra" and opcion == "papel":
    x += 1
    tu += 1
    print ("El PC saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
elif azar == "papel" and opcion == "tijera":
    x += 1
    tu += 1
    print ("El PC saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
elif azar == "papel" and opcion == "piedra":
    x += 1
    pc += 1
    print ("El pc saco", azar)
    print ("Tu", tu, "PC", pc)
    ganador(tu,pc)
    print ("")
else:
    print ("Opcion incorrecta, vuleva a intentarlo")

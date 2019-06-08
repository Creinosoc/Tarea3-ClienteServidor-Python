# -*- coding: utf-8 -*-
#!/usr/bin/env python

# http://www.pythondiario.com

import random
from time import sleep

print ("Bienvenido, vamos a jugar a Piedra, papel o tijera.")
print ("")
sleep(2)
print ("Jugamos al mejor de tres, o prefieres cambiar?")
sleep(1)
print ("")


#Funcion que realiza la lógica del juego
def juego(intentos):
 x = 0
 tu = 0
 pc = 0
 while str(x) != intentos:
  print ("Piedra, papel o tijera?")
  opcion = input()
  opcion = opcion.lower()
  azar = random.choice(["piedra", "papel", "tijera"])
  if opcion == azar:
   print ("El pc tambien elijio", azar)
   print ("")
  elif azar == "tijera" and opcion == "papel":
   x += 1
   pc += 1
   print ("El PC saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  elif azar == "tijera" and opcion == "piedra":
   x += 1
   tu += 1
   print ("El PC saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  elif azar == "piedra" and opcion == "tijera":
   x += 1
   pc += 1
   print ("El PC saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  elif azar == "piedra" and opcion == "papel":
   x += 1
   tu += 1
   print ("El PC saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  elif azar == "papel" and opcion == "tijera":
   x += 1
   tu += 1
   print ("El PC saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  elif azar == "papel" and opcion == "piedra":
   x += 1
   pc += 1
   print ("El pc saco", azar)
   print ("Tu", tu, "PC", pc)
   print ("")
  else:
   print ("Opcion incorrecta, vuleva a intentarlo")
 
 print ("")
 
 if pc > tu:
  print ("Gano el PC", pc, "a", tu)
 elif pc == tu:
  print ("Empataron", tu, "a", pc)
 else:
  print ("Ganaste", tu, "a", pc)
 
 print ("")
 print ("PARTIDA TERMINADA")
  
   
def main():
 print ("Escribe 1 para jugar al mejor de tres.")
 print ("Escribe 2 para cambiar el tipo de juego.")

 opcion = input()

 if opcion == 1:
  juego("3")
  print ("")
  restart = input ("Quieres jugar de nuevo?(s/n): ")
  restart = restart.lower()
  if restart == "s":
   print ("")
   main()
 else:
  intentos = input ("Tu diras, jugamos al mejor de: ")
  juego(intentos)
  print ("")
  restart = input ("Quieres jugar de nuevo?(s/n): ")
  restart = restart.lower()
  if restart == "s":
   print ("")
   main()
  else:
   print ("FIN")
   
main()

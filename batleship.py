#!/usr/bin/env python
 # -*-coding: 850 -*-
 
#esos codigos raros de arriva son para que la letra ¤ y las tilden funcionen
 
 
import random #<-------------para generar numeros al azar hasta donde se yo
import os  #<----- para ejercutar comandos de la consola shell, y para otras cosas mas que desconosco
import time #<-------------para detener el programa por tiempos determinados
import sys
#-------------------------------------------------------------------------------
 
#-Tableros
tablero = [[" "," "," ","1","2","3","4","5"],[" ","-------------"],[" ","A","|",'O', 'O', 'O', 'O', 'O'], [" ","B","|",'O', 'O', 'O', 'O', 'O'], [" ","C","|",'O', 'O', 'O', 'O', 'O'], [" ","D","|",'O', 'O', 'O', 'O', 'O'], [" ","E","|",'O', 'O', 'O', 'O', 'O']]
tablero_bot=[[" "," "," ","1","2","3","4","5"],[" ","-------------"],[" ","A","|",'O', 'O', 'O', 'O', 'O'], [" ","B","|",'O', 'O', 'O', 'O', 'O'], [" ","C","|",'O', 'O', 'O', 'O', 'O'], [" ","D","|",'O', 'O', 'O', 'O', 'O'], [" ","E","|",'O', 'O', 'O', 'O', 'O']]
 
#------------------------------------------------------------------------------------------
#-funciones basicas del juego


#Funcion #1 Impresor de tablero (el que lo organiza):
def print_tablero(tablero_a):
  for fila in tablero_a:
    print (" ".join(fila)) #la funcion join()  nos permite eliminar las " , " de las listas.
 
 
 
#print_tablero(tablero_bot)  <----tablero de bot
 
#-----------------------------------------------------------------------------------------------------------
 
 
#Funcion #2 generador de posicion del enemigo:
 
def fila_aleatoria(tablero_bot):
  return random.randint(2,len(tablero_bot)-1)
 
def columna_aleatoria(tablero_bot):
        return random.randint(3,len(tablero_bot[0])-1)
 
#barco_fila = fila_aleatoria(tablero_bot)
#barco_col = columna_aleatoria(tablero_bot)
 
#Funcion #3 generador de coordenadas de jugador: esta funcion transforma las coordenadas que inserta el jugador "a1, a2, b3" etc a numeros para hubicarnos dentro de las listas donde estan los tableros.
def coordenadas_barco(y):
    coordenada=[]
    if len(y)==2:
        y=y.lower()
        if y[0]=="a" or y[0]=="b" or y[0]=="c" or y[0]=="d" or y[0]=="e":
            if y[1]=="1" or y[1]=="2" or y[1]=="3" or y[1]=="4" or y[1]=="5":
                if y[0]=="a":
                    coordenada.append(2)
                    coordenada.append(int(y[1])+2)
                    coordenada.append("Muy bien") #el "Muy bien" se envia para como mensaje para decir "que las coordenadas estan bien"
 
                elif y[0]=="b":
                    coordenada.append(3)
                    coordenada.append(int(y[1])+2)
                    coordenada.append("Muy bien")
                elif y[0]=="c":
                    coordenada.append(4)
                    coordenada.append(int(y[1])+2)
                    coordenada.append("Muy bien")
                elif y[0]=="d":
                    coordenada.append(5)
                    coordenada.append(int(y[1])+2)
                    coordenada.append("Muy bien")
                else:
                    coordenada.append(6)
                    coordenada.append(int(y[1])+2)
                    coordenada.append("Muy bien")
                return coordenada
            else:
                coordenada=[None,None,"Muy bien"] #el "Muy bien" significa que hay un error en la coordenada
                return coordenada
 
        else:
            coordenada=[None,None,"Muy bien"]
            return coordenada
    else:
        coordenada=[None,None,"Muy bien"]
        return coordenada
 
 
 
#Funcion #4 generador posicion del jugador:-------------------------------------------------------------------------------------------------------------------
 
def posicion_jugador():  #aqui insertamos la coordenada "a1,a2 etc" que se envia a la funcion de arriba para transformarla a la coordenada dentr de las listas
    while True:
        print ("\n")
        print ("-Ingrese la coordenada donde quiere ocultar su barco")
        coordenada_jugador= input("--->: ")
        coordenada_jugador=coordenadas_barco(coordenada_jugador) #<----- ahi esta la funcion de arriba
        if coordenada_jugador[2]=="Muy bien":
            return coordenada_jugador
            break
        else:
            print(" ")
            print ("Coordenada invalida \n")
 
 
#coordenada_jugador=posicion_jugador()
#jugador_fila_lugar=coordenada_jugador[0]
#jugador_col_lugar=coordenada_jugador[1]
 
 
#Funcion #5 generador posicion jugador2-----------------------------------------------------------------------------------------------------
#si se juega multiplayer esto hace lo mismo que la funcion de arriba pero para el player 2
def posicion_jugador2():
    while True:
        print ("\n")
        print ("-Ingrese la coordenada donde quiere ocultar su barco")
        coordenada_jugador2= input("--->: ")
        coordenada_jugador2=coordenadas_barco(coordenada_jugador2)
        if coordenada_jugador2[2]=="Muy bien":
            return coordenada_jugador2
            break
        else:
            print(" ")
            print ("-Coordenada invalida \n")
 
#coordenada_jugador2=posicion_jugador2()
#jugador_fila_lugar2=coordenada_jugador2[0]
#jugador_col_lugar2=coordenada_jugador2[1]
 
 
#Motor de ataque-------------------------------------------------------------------
 
#Funcion #6 ataque de jugador
 
def ataque_jugador():
    while True:
        print ("\n")
        print ("Ingrese la coordenada del lugar a donde desea disparar sus ca¤ones")
        coordenada_jugador= input("--->: ")
        coordenada_jugador=coordenadas_barco(coordenada_jugador)
        if coordenada_jugador[2]=="Muy bien":
            return coordenada_jugador
            break
        else:
            print(" ")
            print ("Bot_Ayuda: Error, ingrese una coordenada valida porfavor!, no te cuesta nada\n")
 
#coordenada_jugador=ataque_jugador()
#jugador_fila=coordenada_jugador[0]
#jugador_col=coordenada_jugador[1]
 
 
 
#Funcion #7 -------en la funci¢n ataque se analiza que pasa con el el ataque del jugador: si da al blanco, si falla etc
def ataque(jugador_fila,jugador_col,barco_fila,barco_col, tablero):
    ataque=0
    if barco_fila == jugador_fila and barco_col == jugador_col:
        tablero[jugador_fila][jugador_col]="W"
        os.system("cls")
        print (" ")
        print_tablero(tablero)
        print ("\nBot_Enemigo: felicidades hundiste mi %$#&%$/# barco\n")
        print ("-------------------------------------------------")
        print ("-               Has ganado                      -")
        print ("-------------------------------------------------")
        print (" ")
        rrrr= input("Precione ENTER para volver al men£ principal")
        ataque=1
        return ataque #nuestra amiga: ataque se encarga de llevar en mensaje de que alguien gan¢ la partida para dar fin al juego
 
    elif tablero[jugador_fila][jugador_col] =="X":
        print ("\nBot_Enemigo: Acaso est s ciego o que? Ya ingresaste esa , pierdes el turno por despistado :)\n")
    else:
        tablero[jugador_fila][jugador_col]="X"
        print("\nBot_Enemigo: Fallaste : Que mala punteria tienes, mejor vete a tu casa a llorar  \n")
 
#ganador=ataque()
 
 
 
 
#Funcion #8 funcion ataque jugador1cuando se juega para dos jugadores playerVsplayer-----------
 
def ataque1(jugador_fila,jugador_col,jugador_fila_lugar2,jugador_col_lugar2,tablero):
    ataque=0
    if jugador_fila_lugar2 == jugador_fila and jugador_col_lugar2 == jugador_col:
        tablero[jugador_fila][jugador_col]="W"
        os.system("cls")
        print (" ")
        print (" ")
        print_tablero(tablero)
        print ("\n---->  Felicidades, has ganado !\n")
        print ("-----------------------------------------------------")
        print ("-            Jugador1 Gana la partida               -")
        print ("-----------------------------------------------------\n")
        print (" ")
        ataque=1
        return ataque #nuestra amiga: ataque se encarga de llevar en mensaje de que alguien gan¢ la partida para dar fin al juego
 
    elif tablero[jugador_fila][jugador_col] =="X":
        print ("\n Acaso est s ciego o que? Ya ingresaste esa , pierdes el turno por despistado :)\n")
    else:
        print ("\nFallaste  \n")
        tablero[jugador_fila][jugador_col]="X"
        input("Precione ENTER para continuar")
 
#ganador=ataque1()
 
 
 
 
#Funcion #9 funcion ataque & ataque jugador 2--------
 
def ataque_jugador2():
    while True:
        print ("\n")
        print ("-Ingrese la coordenada del lugar a donde quiera disparar sus ca¤ones")
        coordenada_jugador2= input("--->: ")
        coordenada_jugador2=coordenadas_barco(coordenada_jugador2)
        if coordenada_jugador2[2]=="Muy bien":
            return coordenada_jugador2
            break
        else:
            print(" ")
            print ("\n--> Error, ingrese una coordenada valida porfavor!, no te cuesta nada\n")
 
#coordenada_jugador2=ataque_jugador2()
#jugador_fila2=coordenada_jugador2[0]
#jugador_col2=coordenada_jugador2[1]
 
 
#Funcion #10 funcion ataque jugador2--------------------
 
 
 
def 2(jugador_fila2,jugador_col2,jugador_fila_lugar,jugador_col_lugar,tablero_bot):
    =0
    if jugador_fila2 == jugador_fila_lugar and jugador_col_lugar == jugador_col2:
        tablero_bot[jugador_fila2][jugador_col2]="W"
        os.system("cls")
        print (" ")
        print (" ")
        print_tablero(tablero_bot)
        print ("\n----> Felicidades, has ganado. \n")
        print ("-----------------------------------------------------")
        print ("-            Jugador1 Gana la partida               -")
        print ("-----------------------------------------------------")
        ataque=1
        return ataque #nuestra amiga: ataque se encarga de llevar en mensaje de que alguien gan¢ la partida para dar fin al juego
 
    elif tablero_bot[jugador_fila2][jugador_col2] =="X":
        print ("\n ---> Acaso estas ciego o que? Ya ingresaste esa , pierdes el turno por despistado :)\n")
    else:
        print ("\nFallaste  \n")
        tablero_bot[jugador_fila2][jugador_col2]="X"
        input("Precione ENTER para continuar")
 
 
#ganador=ataque1()
 
 
 
#Funcion #11 ataque de bot-------------------------------
 
#estas funciones generan el ataque aleatorio del bot, aun sobran porque dentro de la funcion ataque_de_bot estan incluidas.
 
def fila_ataque_bot1(tablero_bot):
  return random.randint(2,len(tablero_bot)-1)
 
def columna_ataque_de_bot1(tablero_bot):
        return random.randint(3,len(tablero_bot[0])-1)
 
#fila_ataque_bot=fila_ataque_bot1(tablero_bot)
#columna_ataque_de_bot=columna_ataque_de_bot1(tablero_bot)
 
#Funcion #13
def porqueria_de_bot(jugador_fila_lugar,jugador_col_lugar,tablero_bot): #esto hace lo mismo que la funcion ataque, solo que en favor del bot.
    print (" ")
    print_tablero(tablero_bot)
    time.sleep(1)
 
    while True:
        fila_ataque_bot=random.randint(2,len(tablero_bot)-1)#
        columna_ataque_de_bot=random.randint(3,len(tablero_bot[0])-1)
        if tablero_bot[fila_ataque_bot][columna_ataque_de_bot] !="X":
            break
    os.system("cls")
    print ("\n------------Turno de tu enemigo---------------\n")
    if fila_ataque_bot == jugador_fila_lugar and columna_ataque_de_bot == jugador_col_lugar:
        tablero_bot[fila_ataque_bot][columna_ataque_de_bot] ="W"
        os.system("cls")
        print (" ")
        print_tablero(tablero_bot)
        print ("\nBot: Acabo de undir tu varco de papel jaja.\n\n ")
        print ("---------------------------------------")
        print ("-             Has Perdido             -")
        print ("---------------------------------------")
        rrrr= input("\n\nPrecione ENTER para volver al men£ principal")
        ataque=1
        return ataque
    else:
        tablero_bot[fila_ataque_bot][columna_ataque_de_bot]="X"
        palabra= ["\nBot_Enemigo: Rayos!, he fallado! \n\n","\nBot_Enemigo: Rayos, no te di :( \n\n","\nBot_Enemigo: Que porqueria! he fallado! \n\n", "\nBot_Enemigo: He fallado, rayos :(\n\n","\nBot_Enemigo: Maldicion, He fallado :(\n\n","\nBot_Enemigo: no te di :(\n\n"]
        botsays= random.randint(0,5)  #<--- hay algunos mensajes que se imprimen al azar cuando el bot falla el disparo
        palabra1=palabra[botsays]
        print (" ")
        print_tablero(tablero_bot)
        print (palabra1)
        time.sleep(1)
 
 
#ganador2=porqueria_de_bot(jugador_fila_lugar,jugador_col_lugar)
 
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#funciones bot vs bot
 
#posiciones bot ----
 
#en las funciones siguientes ordeno a un bot que juegue contra otro (porque no experimentar esto tambi‚n) xD
#Funcion #14
def posicion_bot1():
    while True:
        print ("\n")
        print ("-Ingrese la coordenada donde quiere ocultar el barco del primer bot")
        coordenada_bot1= input("--->: ")
        coordenada_bot1=coordenadas_barco(coordenada_bot1)
        if coordenada_bot1[2]=="Muy bien":
            return coordenada_bot1
            break
        else:
            print(" ")
            print ("Coordenada invalida \n")
 
 
#coordenada_bot1=posicion_bot1()
#bot1_fila_lugar=coordenada_bot1[0]
#bot1_col_lugar=coordenada_bot1[1]
 
 
#si nos da flojera elejir las coordenadas de los bots, pues dejemos que ellos lo hagan
 
#bot1_fila_lugar = fila_aleatoria(tablero)
#bot1_col_lugar = columna_aleatoria(tablero)
#Funcion #15
def posicion_bot2():
    while True:
        print ("\n")
        print ("Ingrese la coordenada donde quiere ocultar el barco del segundo bot bot")
        coordenada_bot2= input("--->: ")
        coordenada_bot2=coordenadas_barco(coordenada_bot2)
        if coordenada_bot2[2]=="Muy bien":
            return coordenada_bot2
            break
        else:
            print(" ")
            print ("Coordenada invalida \n")
 
 
#coordenada_bot2=posicion_bot2()
#bot2_fila_lugar=coordenada_bot2[0]
#bot2_col_lugar=coordenada_bot2[1]
 
 
 
#si la selecion es automatica
 
#bot2_fila_lugar = fila_aleatoria(tablero)
#bot2_col_lugar = columna_aleatoria(tablero)
 
 
#ataque bot1----------------
 
#supongo que ya saben masomenos para que sirven las funciones ataque xD
 
#Funcion #16
def porqueria_de_bot1(bot2_fila_lugar,bot2_col_lugar, tablero_bot):
    while True:
        fila_ataque_bot1=random.randint(2,len(tablero_bot)-1)
        columna_ataque_de_bot1=random.randint(3,len(tablero_bot[0])-1)
        if tablero_bot[fila_ataque_bot1][columna_ataque_de_bot1] !="X":
            break
    if fila_ataque_bot1 == bot2_fila_lugar and columna_ataque_de_bot1 == bot2_col_lugar:
        tablero_bot[fila_ataque_bot1][columna_ataque_de_bot1] ="W"
        print_tablero(tablero_bot)
        print ("-------------------------------------------")
        print ("-             Bot_1 ha ganado             -")
        print ("-------------------------------------------")
        ataque=1
        return ataque
    else:
        tablero_bot[fila_ataque_bot1][columna_ataque_de_bot1]="X"
        print_tablero(tablero_bot)
 
 
 
#ganador1=porqueria_de_bot1(bot2_fila_lugar,bot2_col_lugar)
 
#ataque bot2----------------
 
 
#Funcion #17
 
def porqueria_de_bot2(bot1_fila_lugar,bot1_col_lugar,tablero):
    while True:
        fila_ataque_bot2=random.randint(2,len(tablero)-1)
        columna_ataque_de_bot2=random.randint(3,len(tablero[0])-1)
        if tablero[fila_ataque_bot2][columna_ataque_de_bot2] !="X":
            break
    if fila_ataque_bot2 == bot1_fila_lugar and columna_ataque_de_bot2 == bot1_col_lugar:
        tablero[fila_ataque_bot2][columna_ataque_de_bot2] ="W"
        print_tablero(tablero)
        print ("-------------------------------------------")
        print ("-             Bot_2 ha ganado             -")
        print ("-------------------------------------------")
        ataque=1
        return ataque
    else:
        tablero[fila_ataque_bot2][columna_ataque_de_bot2]="X"
        print_tablero(tablero)
 
 
 
#ganador2=porqueria_de_bot2(bot1_fila_lugar,bot1_col_lugar)
 
 
 
 
 
 
 
 
#-------------------------------------------------------------------------
#Funcion jugador vs bot----------------------------------------------------
#aqui empezamos a armar los modos de juego juntando todas las funciones anteriores en 1, este es para jugar player vs bot
#Funcion #18
 
def jugadorVSbot(tablero,tablero_bot):
 
    print (" ")
    print_tablero(tablero)
    coordenada_jugador=posicion_jugador()
    jugador_fila_lugar=coordenada_jugador[0]
    jugador_col_lugar=coordenada_jugador[1]
    #coordenadas bot
    barco_fila = fila_aleatoria(tablero_bot)
    barco_col = columna_aleatoria(tablero_bot)
    while True:
        #juego
        os.system("cls")
        print ("\n----------Turno Jugador1--------------------------------\n")
        print_tablero(tablero)
        coordenada_jugador=ataque_jugador()
        jugador_fila=coordenada_jugador[0]
        jugador_col=coordenada_jugador[1]
        ganador=ataque(jugador_fila,jugador_col,barco_fila,barco_col, tablero)
        if ganador==1:
            ataque1=1
            return ataque1
            input("Precione ENTER para volver al men£ principal")
            print (" ")
            break
 
        else:
            input("Precione ENTER para continuar")
        os.system("cls")
        print ("\n------------Turno de tu enemigo---------------\n")
 
        ganador2=porqueria_de_bot(jugador_fila_lugar,jugador_col_lugar,tablero_bot)
        if ganador2==1:
            ataque1=1
            return ataque1
            input("Precione ENTER para volver al men£ principal")
            break
        else:
            input("Precione ENTER para continuar\n")
 
 
 
 
#funcion jugador vs jugador-----------------------------------------------------------
#Funcion #19
def JugadorVsJugador(tablero,tablero_bot):
    #coordenadas jugador1
    print ("\n---------Jugador1------------------\n")
    print_tablero(tablero)
    print (" ")
    coordenada_jugador=posicion_jugador()
    jugador_fila_lugar=coordenada_jugador[0]
    jugador_col_lugar=coordenada_jugador[1]
    #coordenadas jugador2
    os.system("cls")
    print ("\n----------jugador2------------------\n")
    print_tablero(tablero_bot)
    print (" ")
    coordenada_jugador2=posicion_jugador2()
    jugador_fila_lugar2=coordenada_jugador2[0]
    jugador_col_lugar2=coordenada_jugador2[1]
    #juego
    while True:
        os.system("cls")
        print ("\n-----------Turno Jugador1----------------\n")
        print_tablero(tablero)
        coordenada_jugador=ataque_jugador()
        jugador_fila=coordenada_jugador[0]
        jugador_col=coordenada_jugador[1]
        ganador=ataque1(jugador_fila,jugador_col,jugador_fila_lugar2,jugador_col_lugar2,tablero)
        if ganador ==1:
            input("Precione ENTER para volver al men£ principal")
            break
 
        os.system("cls")
        print ("\n-----------Turno Jugador2---------------\n")
        print_tablero(tablero_bot)
        coordenada_jugador2=ataque_jugador2()
        jugador_fila2=coordenada_jugador2[0]
        jugador_col2=coordenada_jugador2[1]
        ganador2=ataque2(jugador_fila2,jugador_col2,jugador_fila_lugar,jugador_col_lugar,tablero_bot)
        if ganador2==1:
            input("Precione ENTER para volver al men£ principal")
            break
 
 
#Funcion #20 funcion botVsbot
 
def botVSbot(tablero,tablero_bot):
    print ("\n------------Elija un modo, Escriba 1 o 2----------\n")
    while True:
        print (" 1-Manual (usted elije la ubicacion de los bots)")
        print (" 2-Automatico (Los Bots elijen una ubicacion a su antojo)")
        shit=input("------->: ")
        if shit =="1":
            os.system("cls")
 
            #bot1
            print (" ")
            print_tablero(tablero)
            coordenada_bot1=posicion_bot1()
            bot1_fila_lugar=coordenada_bot1[0]
            bot1_col_lugar=coordenada_bot1[1]
            #bot2
            coordenada_bot2=posicion_bot2()
            bot2_fila_lugar=coordenada_bot2[0]
            bot2_col_lugar=coordenada_bot2[1]
            print ("\nEl juego comienza en: \n")
 
            time.sleep(1)
            print ("------>: 3\n")
            time.sleep(1)
            print("------>: 2\n")
            time.sleep(1)
            print ("------>: 1\n")
            time.sleep(1)
            break
 
 
 
 
        elif shit=="2":
            os.system("cls")
            print (" ")
 
            #bot1
            bot1_fila_lugar = fila_aleatoria(tablero)
            bot1_col_lugar = columna_aleatoria(tablero)
            #bot2
            bot2_fila_lugar = fila_aleatoria(tablero)
            bot2_col_lugar = columna_aleatoria(tablero)
            print ("\nEl juego comienza en: \n")
 
            time.sleep(1)
            print ("------>: 3\n")
            time.sleep(1)
            print("------>: 2\n")
            time.sleep(1)
            print ("------>: 1\n")
            time.sleep(1)
            break
        else:
            print ("\n-->Elija una obcion valida<----\n")
 
    while True:
 
 
        print ("\n--------Turno Bot_1--------------\n")
        ganador1=porqueria_de_bot1(bot2_fila_lugar,bot2_col_lugar,tablero_bot)
        if ganador1==1:
            input("Precione ENTER para volver al men£ principal\n")
            print (" \n.")
 
            break
        print ("\n--------Turno Bot_2--------------\n")
        ganador2=porqueria_de_bot2(bot1_fila_lugar,bot1_col_lugar,tablero)
        if ganador2==1:
            input("Precione ENTER para volver al men£ principal\n")
            print (" \n.")
 
            break
 
 
#motor del juego
#y la funcion main que ejecuta todo el juego
#Funcion #21
 
 
 
 
 
 
def main():
    os.system("color 2")
    print ("----------------------------------------------------")
    print ("-             Bienvenid@ a batalla naval           -")
    print ("----------------------------------------------------")
 
    time.sleep(1)
    while True:
        tablero = [[" "," "," ","1","2","3","4","5"],[" ","-------------"],[" ","A","|",'O', 'O', 'O', 'O', 'O'], [" ","B","|",'O', 'O', 'O', 'O', 'O'], [" ","C","|",'O', 'O', 'O', 'O', 'O'], [" ","D","|",'O', 'O', 'O', 'O', 'O'], [" ","E","|",'O', 'O', 'O', 'O', 'O']]
        tablero_bot=[[" "," "," ","1","2","3","4","5"],[" ","-------------"],[" ","A","|",'O', 'O', 'O', 'O', 'O'], [" ","B","|",'O', 'O', 'O', 'O', 'O'], [" ","C","|",'O', 'O', 'O', 'O', 'O'], [" ","D","|",'O', 'O', 'O', 'O', 'O'], [" ","E","|",'O', 'O', 'O', 'O', 'O']]
 
 
        print ("\n------------------Menu Principal-----------------------------------------\n")
        print ("Selecione el modo de juego (Escriba 1,2,3... segun lo que se le antoje)")
        print (" ")
        print (" ")
        print (" 1-Single player.")
        print (" 2-Multiplayer (Sin revisar, puede contener errores).")
        print (" 3-Bot Vs Bot \n")
        selecciion1=input("------->: ")
        if selecciion1=="1":
            os.system("cls")
            jugadorVSbot(tablero,tablero_bot)
 
        elif selecciion1=="2":
            os.system("cls")
            JugadorVsJugador(tablero,tablero_bot)
        elif selecciion1=="3":
            os.system("cls")
            botVSbot(tablero,tablero_bot)
 
        else:
            print ("\n ---->>Ingrese una obcion valida<<---")
            time.sleep(1.5)
        os.system("cls")
 
 
 
main()
 

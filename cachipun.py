#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from random import randint
 
def juegoPPT(nums = 0, rein = False):
    if rein == False: print('-- Bienvenido al juego de piedra, papel o tijera --')
    if (nums == 0):
        nums = input('Establezca el numero de partidas que se deben ganar para terminar el juego: ')
        if (len(nums) < 1):
            print('Por defecto la partida sera solo una')
            nums = 1
        elif (int(nums) == 0):
            print('Numero de partidas no validas, intentalo de nuevo')
            return juegoPPT(0, True)
    partidas = (int(nums)*2) - 1
    if (int(nums) > 1 and rein == False): print('Basado en el numero de partidas a ganar, el total a jugar seran %s partidas' % partidas)
    print("--------------------------------------------------------")
    print("-------------------Opciones-----------------------")
    print("----------piedra, papel o tijera-----------------")
    print("--------------------------------------------------------")
    print('')
    ganador = [0, 0]
    finalizo = False
    opciones = ['piedra', 'papel', 'tijera']
    resultados = [ [False, False, True], [True, False, False], [False, True, False] ]
    while partidas:
        opcion = input('Ingrese su comodin : ')
        if opcion not in opciones:
            print('Lo siento, %s no es un comodin valido para el juego, intentalo de nuevo\n' % opcion)
        else:
            opcion_pc = randint(0,2)
            opcion_us = opciones.index(opcion)
            print ('PC: %s vs TU: %s' % (opciones[opcion_pc],opcion) )
            if (opcion_pc == opcion_us):
                print('No hay ganador\n')
            else:
                if resultados[opcion_pc][opcion_us]:
                    ganador[0] += 1
                    if (int(nums) > 1): print('Perdiste la partida\n')
                else:
                    ganador[1] += 1
                    if (int(nums) > 1): print('Ganaste la partida\n')
            if (int(nums) in ganador):
                ganador_juego = 'Ganaste el juego\n' if (ganador.index(int(nums)) == 1) else '\nLa PC gano el juego\n'
                print (ganador_juego)
                finalizo = True
                break
            elif (partidas == int(nums) and sum(ganador) == 0): break
            partidas -= 1
    if (finalizo != True): print('Partidas terminadas sin ganador o es posible que no haya algun ganador en las siguientes')
    if (input('¿Quiere volver a jugar? (S/N): ').lower() == 's'):
        print('')
        return juegoPPT()
    else:
        print('\nJuego terminado.....')

juegoPPT()

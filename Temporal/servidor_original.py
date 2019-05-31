#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa Servidor

import socket
import sys
import random

#-------------------------------------------------------
caras = 6
dado1 = []
dado2 = []
intentos = 3

def dado(dado,n_intentos):
    suma = 0
    for i in range(0, n_intentos):
        print ("Tiro el dado ",i+1," veces")
        dado.append(random.randint(1,caras))
        print ("Dado 1 = ", dado)
        suma = suma + dado[i]

    print ("Total = ",suma)


dado(dado1,intentos)
#-------------------------------------------------------

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio.")
    sys.exit(0)

IP = "192.168.122.89"
IPLocal = "localhost"
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, " ...")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IPLocal, PUERTO))
# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(4)

print ("Servicio configurado.\n")

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto

        #Jugardor 1
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ",direccion_cliente)

        # Jugardor 2
        # socket_cliente, direccion_cliente = socket_servidor.accept()
        # print "Cliente conectado desde: ",direccion_cliente

        while True:
            try:
                recibido = socket_cliente.recv(1024)
                print (str(direccion_cliente[0]) + " >> ", recibido)
                if recibido == "finalizar()":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                respuesta_servidor = str(direccion_cliente[0]) + " envio: " + recibido
                socket_cliente.send(respuesta_servidor.encode("utf-8"))
                socket_servidor

            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")

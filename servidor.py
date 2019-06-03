import time, socket, sys
import random

#-------------------------------------------------------
caras = 6
dado1 = []
dado2 = []

intentos = 3

def dado_imprimir(dado,intentos):
	sum=0
	for i in range(intentos):
		print("tiro el dado",i+1,"veces")
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
		print("dado 1 = ",dado)
	print("la suma de sus tiradas es = ",sum)

def dado_calcular(dado,intentos):
	sum=0
	for i in range(intentos):
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
	return sum


# dado(dado1,intentos)
#-------------------------------------------------------

print('Configurando Servidor...')
time.sleep(3)
#Get the hostname, IP Address from socket and set Port

soc = socket.socket()
host_name = "Sr servidor"
IP = "localhost"
# IP = socket.gethostbyname(host_name)
PUERTO = 9090
soc.bind((IP, PUERTO))
print(host_name, '(IP = {})'.format(IP))
# name = input('Enter name: ')
name = "Sr Servidor"
soc.listen(1) #Try to locate using socket
print('Esperando conexiones...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Conexion establecida. conectado desde: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(2048)
client_name = client_name.decode()
print(client_name + ' El cliente se a conectado.')
print('Escriba <<salir()>> para Cerrar el servicio')
connection.send(name.encode())

# saludo1 = print('wena lo chicabros')

while True:

    mensaje = 'Bienvenido'
    # message = input(dado(dado1,intentos))
    if mensaje == 'salir()':
        mensaje = 'Good Night...'
        connection.send(mensaje.encode())
        print("\n")
        break
    if mensaje == 'Bienvenido':
        mensaje = '--Bienvenido a la sala de juegos--\n1.- Juegos de dados\n2.- ...'
        connection.send(mensaje.encode())
        mensaje = connection.recv(1024)
        mensaje = mensaje.decode()
        print("Cliente -",client_name,">>",mensaje)

        if mensaje == '1':
            mensaje = '--Juegos de dados--\n>> Lanzaras 3 veces un dado de 6 caras, aquel que saque el mayor gana\nPRECIONE UNA TECLA PARA CONTINUAR'
            connection.send(mensaje.encode())
            mensaje = connection.recv(2048)
            mensaje = mensaje.decode()
            print("Cliente -",client_name,">>",mensaje)
			j2 = dado_calcular(dado1,intentos)

			if mensaje > j2 :
				mensaje = "Gano el Jugador 1 con {}".format(j1)
			else:
				mensaje = "Gano el cliente con {}".format(mensaje)

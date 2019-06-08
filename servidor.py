import time, socket, sys
import random
from time import sleep
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

def dado_clear(arg):
	pass

# dado(dado1,intentos)
#-------------------------------------------------------

def cachipum():
	mano_servidor = random.choice(["piedra", "papel", "tijera"])

	return mano_servidor


#-------------------------------------------------------

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio.")
    sys.exit(0)

IP = "192.168.122.89"
IPLocal = "localhost"
PUERTO = int(sys.argv[1])

print('Configurando Servidor...')
time.sleep(2)
#Get the hostname, IP Address from socket and set Port

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# soc = socket.socket()
host_name = "Sr servidor"
IP = "localhost"
# IP = socket.gethostbyname(host_name)
socket_servidor.bind((IPLocal, PUERTO))
# soc.bind((IP, PUERTO))
print(host_name, '(IP = {})'.format(IP))
# name = input('Enter name: ')
name = "Sr Servidor"
socket_servidor.listen(1) #Try to locate using socket
print('Esperando conexiones...')


# saludo1 = print('wena lo chicabros')
try:
	while True:
		connection, addr = socket_servidor.accept()
		print("Received connection from ", addr[0], "(", addr[1], ")\n")
		print('Conexion establecida. conectado desde: {}, ({})'.format(addr[0], addr[0]))
		#get a connection from client side
		client_name = connection.recv(2048)
		client_name = client_name.decode()
		print(client_name + ' El cliente se a conectado.')
		connection.send(name.encode())
		while True:
			try:
				mensaje = 'volver'
    			# message = input(dado(dado1,intentos))
				if mensaje == 'salir()':
					mensaje = 'Nos vemos Gracias por jugar!...'
					connection.send(mensaje.encode())
					print("\n")
					break

				if mensaje == 'volver':
					mensaje = '---Bienvenido a la sala de juegos---\n1.- Juegos de dados\n2.- Cachipun \n3.- Salir'
					connection.send(mensaje.encode())
					mensaje = connection.recv(2048)
					mensaje = mensaje.decode()
					print("Cliente -",client_name,">>",mensaje)

					if mensaje == '1':
						dado1 = []
						j2 = dado_calcular(dado1,intentos)
						mensaje = '--Juegos de dados--\n>> Lanzaras 3 veces un dado de 6 caras, aquel que saque el mayor gana\nPRECIONE UNA TECLA PARA CONTINUAR'
						connection.send(mensaje.encode())
						mensaje = connection.recv(2048)
						mensaje = mensaje.decode()
						print("Cliente -",client_name,">>",mensaje)

						mensaje = connection.recv(2048)
						mensaje = mensaje.decode()
						# mensaje = int(mensaje)#"{}".format(mensaje)
						print("Cliente -",client_name,">>",mensaje)
						print("Servidor -",j2)
						if int(mensaje) > j2 :
							mensaje = "Gano el Cliente con {}\n Escriba <volver>, para volver al menu :D".format(mensaje)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						else:
							mensaje = "Gano el Servidor con {}\n Escriba <volver>, para volver al menu :D".format(j2)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)

					if mensaje == '2':
						mensaje = "---Cachipum---\n>> Bienvenido, vamos a jugar a Cachipum.\n>> Juguemos!!!.\n>> Elije: piedra, papel o tijera?"
						resultado = cachipum()
						connection.send(mensaje.encode())
						mensaje = connection.recv(2048)
						mensaje = mensaje.decode()
						print("Cliente -",client_name,">>",mensaje)
						print("Servidor -",resultado)

						if mensaje == resultado:
							mensaje = "El pc tambien elijio {}, es un empate\n Escriba volver".format(resultado)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "tijera" and mensaje == "papel":
							mensaje = "Gano el Servidor jaja - {}\n Escriba <volver>, para volver al menu :D".format(resultado)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "tijera" and mensaje == "piedra":
							mensaje = "Gano el Cliente - {}\n Escriba <volver>, para volver al menu :D".format(mensaje)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "piedra" and mensaje == "tijera":
							mensaje = "Gano el Servidor jaja - {}\n Escriba <volver>, para volver al menu :D".format(resultado)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "piedra" and mensaje == "papel":
							mensaje = "Gano el Cliente - {}\n Escriba <volver>, para volver al menu :D".format(resultado)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "papel" and mensaje == "tijera":
							mensaje = "Gano el Cliente - {}\n Escriba <volver>, para volver al menu :D".format(mensaje)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						elif resultado == "papel" and mensaje == "piedra":
							mensaje = "Gano el Servidor jaja - {}\n Escriba <volver>, para volver al menu :D".format(resultado)
							connection.send(mensaje.encode())
							mensaje = connection.recv(2048)
							mensaje = mensaje.decode()
							print("Cliente -",client_name,">>",mensaje)
						else:
							print ("Opcion incorrecta, vuleva a intentarlo")

			except socket.error:
				print ("Conexion terminada abruptamente por el cliente.")
				print ("Cerrando conexion con el cliente ...")
				connection.close()
				print ("Conexion con el cliente cerrado.")
				break

			except KeyboardInterrupt:
			    print ("\n∫Se interrunpio el cliente con un Control_C.")
			    print ("Cerrando conexion con el cliente ...")
			    connection.close()
			    print ("Conexion con el cliente cerrado.")
			    break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")

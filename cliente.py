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
        print("Intento",i+1,":")
        dado.append(random.randint(1,6))
        sum=sum+dado[i]
        print("dado 1 = ",dado)
        time.sleep(1)

    print("la suma total es:",sum)
    time.sleep(2)
    return sum


def dado_calcular(dado,intentos):
	sum=0
	for i in range(intentos):
		dado.append(random.randint(1,6))
		sum=sum+dado[i]
	return sum

#-------------------------------------------------------

#-------------------------------------------------------

print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
PUERTO = 9090

print("\nTrying to connect to ", server_host, "(", PUERTO, ")\n")
# print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, PUERTO))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(2048)
server_name = server_name.decode()
print('{} a entrado...'.format(server_name))
print('Escriba <<salir()>> para salir de la sala')
print('Espere la respuesta del servidor...')

while True:
    dado1 = []
    message = soc.recv(2048)
    message = message.decode()
    print(message)  #imprime el mensaje del servidor
    message = input(str("Yo >> "))
    if message == 'salir()':
        message = 'Leaving the Chat room'
        soc.send(message.encode())
        # print("\n")
        break
    if message == '1':
        message = '1'
        soc.send(message.encode())
        print("\n")
    if message == '':
        j1 = dado_imprimir(dado1,intentos)
        # print ("Has sacado saco un total de : ", j1)
        message = "{}".format(j1)
    soc.send(message.encode())

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

if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.")
    sys.exit(0)

print('Iniciando Sesion CLIENTE...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
# soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = 'IP'.format(IP)
name = input('Ingrese su nombre: ')

# print("\nTrying to connect to ", server_host, "(", PUERTO, ")\n")
# print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
print("Conectando...\n")
socket_cliente.send(name.encode())
server_name = socket_cliente.recv(2048)
server_name = server_name.decode()
print('{} a entrado...'.format(server_name))
print('Escriba <<salir()>> para salir de la sala')
print('Espere la respuesta del servidor...')

try:

    while True:
        dado1 = []
        message = socket_cliente.recv(2048)
        message = message.decode()
        print(message)  #imprime el mensaje del servidor
        message = input(str("Yo >> "))
        if message == 'salir()':
            message = 'Adios!'
            socket_cliente.send(message.encode())
            break

        if message == '1':
            message = '1'
            socket_cliente.send(message.encode())
            print("\n")

        if message == '':
            j1 = dado_imprimir(dado1,intentos)
            # print ("Has sacado saco un total de : ", j1)
            message = "{}".format(j1)


        if message == '2':
            message = '2'
            socket_cliente.send(message.encode())

            message = socket_cliente.recv(2048)
            message = message.decode()
            print(message)  #imprime el mensaje del servidor
            message = input(str("Yo >> "))
            socket_cliente.send(message.encode())

        if message == '3':
            break

        socket_cliente.send(message.encode())

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")

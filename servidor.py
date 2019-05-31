import time, socket, sys
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


# dado(dado1,intentos)
#-------------------------------------------------------

def saludo():
    # s1 = input(f"Dígame su apellido, {nombre}: ")
    # print('_________________________')
    print('Bienvenido al servidor!!!')
    # print('_________________________')

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
print('Escriba <<terminar()>> para salir de la sala')
connection.send(name.encode())

saludo1 = print('wena lo chicabros')

while True:
   message = input('Yo >> ')
   # message = input(dado(dado1,intentos))
   if message == 'terminar()':
      message = 'Good Night...'
      connection.send(message.encode())
      print("\n")
      break
   connection.send(message.encode())
   message = connection.recv(2048)
   message = message.decode()
   print(client_name, '>', message)

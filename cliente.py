import time, socket, sys

#-------------------------------------------------------

def saludo():
    # s1 = input(f"Dígame su apellido, {nombre}: ")
    # print('_________________________')
    print('Bienvenido al servidor!!!')
    # print('_________________________')

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
print('Escriba <<terminar()>> para salir de la sala')
print('Espere la respuesta del servidor...')

while True:
   message = soc.recv(2048)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str("Me > "))
   if message == 'terminar()':
      message = "Leaving the Chat room"
      soc.send(message.encode())
      print("\n")
      break
   soc.send(message.encode())

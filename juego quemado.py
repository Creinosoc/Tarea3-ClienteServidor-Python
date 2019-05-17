import time
nombre = input ("¿Como te llamas?")
print(" ")
print ("Hola, "+nombre,"Es hora de jugar al ahorcado")
print(" ")
time.sleep(1)
print("Comienza a adivinar")
print(" ")
time.sleep(0.5)
palabra ='chile'
palabra1 ='makako'
palabra2 ='kkkkk'
palabra3 ='pip'
palabra4 ='sacerdotes'
palabra5 ='titanes'
palabra6 ='olimpicos'
palabra7 ='caballeros'
palabra8 ='faraones'
palabra9 ='defensores'
palabra10 ='faeries'
lista =['chile','makako','kkkkk','pip','sacerdotes','titanes']

tupalabra= ''
vidas= 5

while vidas > 0:
    
    fallas = 0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*", end="")
            fallas+=1

    if fallas == 0:
        print("")
        print("Felicicades, ganaste")
        break
    
    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Equivocacion")
        print("Tu tienes", +vidas, "vidas")

    if vidas == 0:
        print("Perdiste!")
else:
    print("Gracias por participar")

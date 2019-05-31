import random
 
lista =['bizantinos','celtas','chinos','francos','godos','ingleses','japoneses','mongoles','turcos','vikingos']

civilizacion = random.randint(0, len(lista))
print("",civilizacion )

for i in [0,civilizacion]:
    if i== civilizacion:
        print("la civilizacione es",lista[i])
        



import random

x=random.randint(1,100)
print("Este juego consiste en que vas a tener que adivinar un numero entre el 1 y 100, pero solo tienes 3 oportunidades")
cont=3
while(cont>0):
    n= int(input("Dime un número: "))
    if(n!=x):
        cont=cont-1
        if(cont!=1):
            print("Te quedan",cont,"oportunidades")
        else:
            print("Te quedan",cont,"oportunidad")
    else:
        print("Has acertado el número")
        break

if (cont==0):
    print("El numero era:",x)
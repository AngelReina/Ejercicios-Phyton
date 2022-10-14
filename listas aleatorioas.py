import random

def lista_numeros():
    cont=0
    lst=[]
    while(cont<20):
        num_random=random.randint(0,100)
        cont+=1
        lst.append(num_random)
    return lst

print(lista_numeros())
print("La longitud es",len(lista_numeros()))
print("El tipo de la lista es",type(lista_numeros()))
#Importo el random
import random
#Hago lo que me pide

def lista_numeros():
    cont=0
    lst=[]
    while(cont<20):
        num_random=random.randint(0,100)
        cont+=1
        lst.append(num_random)
    return lst
# Muestro el resultado


"""
print("La longitud es",len(lista_numeros()))
print("El tipo de la lista es",type(lista_numeros()))
"""
# filtra_lista_pares([1,2,3,4])
# devuelve ---> [2,4]

def filtra_lista_pares(lst):
    lst_pares=[]
    for i in lst:
       if(i%2==0):
            lst_pares.append(i)
    return lst_pares

       
           

'''
Definir una función que dado una lista y un número
devuelva
   - True si se encuentra el número en la lista
   - False e.c.c.
'''
lista = lista_numeros()
print(lista)
num= int(input("Dime un número: "))
def busqueda_num(lst, num):
    if(num in lst):
       return True
    else:
       return False

print(busqueda_num(lista,num))
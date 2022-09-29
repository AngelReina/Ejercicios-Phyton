# Imprimir en pantalla el número mayor y el número menor de una serie
# de cinco números enteros que vamos introduciendo por teclado.

# Definir variables
import math
num = -1
cont = 5
minimo = math.inf
maximo = -1 * math.inf

# Hago el problema 
while(cont>=1):
    print("Introduzca un número ")
    num = int(input())
    if(num< minimo):
        minimo=num
    if(num>maximo):
        maximo=num
    cont= cont-1
    
# Muestro el resultado
print("El número mayor de la serie de 5 números es: ",maximo)  
print("El número menor de la serie de 5 números es: ",minimo) 

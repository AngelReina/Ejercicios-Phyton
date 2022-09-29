# Introduciendo un número en el teclado de ordenador, hallar cuantos
# números enteros múltiplos de tres, hay comprendidos entre la unidad y dicho número.

# Definir variables
num= -1
res = 0
indice = 1

# Pregunto al usuario
print("Introduzca un número ")
num = int(input())

# Hago el problema  
while(indice <= num):
    if (indice % 3 == 0):
        res = res + 1
    
    indice= indice+1   

# Muestro el resultado
print("Desde ",num,"hasta la unidad hay un toltal de: ",res,"múltiplos")
    

          
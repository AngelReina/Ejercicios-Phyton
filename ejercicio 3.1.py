#  Introduciendo un número en el teclado, imprimir la tabla de multiplicar de dicho número.

# Definir variables
indice=0
num= -1
res= -1

# Pregunto al usuario
print("¿Qué tabla de multiplicar quieres? ")
num = int(input())
print("La tabla de multiplicar del", num, "es:")

# Hago el problema
while(indice <= 10):
    res= num * indice
    print(num, "*" ,indice, "=" ,res,)
    indice = indice+1
    
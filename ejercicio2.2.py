# Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, liquido, vapor) en función de su temperatura.

# Definir variables
edad = 0

# Preguntar al usuario por los datos
print("Introduca la edad del niño ")
edad = int(input())

# Hago el problema
if (edad < 6):
 print ( " El niño no tiene categoría deportiva")
elif (edad == 6 or edad == 7):
 print ( "La categoria del niño es benjamín")   
elif ( edad == 8 or edad == 9):
 print ( "La categoria del niño es alevín")
elif (edad == 10 or edad == 11):
 print ( "La categoria del niño es infantil")
elif ( edad >= 12):
 print ( "La categoria del niño es cadete")
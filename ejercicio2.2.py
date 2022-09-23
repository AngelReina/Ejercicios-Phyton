# Escriba un algoritmo que determine la categoría deportiva de un usuario
# en función de su edad.
# - 6 a7 años: “benjamin”
# - 8 a 9 años: “ alevín”
# - 10 a 11 años: “infantil”
# - 12 años y más: “cadete”

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
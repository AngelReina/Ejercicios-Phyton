# Escriba, usando comparaciones, un algoritmo que muestre el estado del agua (hielo, liquido, vapor) en función de su temperatura.

# Definir variables
agua = 0

# Preguntar al usuario por los datos
print("Introduca a que temperatura esta el agua ")
agua = float(input())

# Hago el problema
if (agua < 10):
 print ( " El agua esta en estado sólido")
elif (agua == 10 or agua < 150):
 print ( "El agua esta en estado líqido")   
elif ( agua >= 150):
    print ( "El agua esta en estado gaseoso")   

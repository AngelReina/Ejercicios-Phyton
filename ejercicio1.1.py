#Introduciendo la hora del día en horas, minutos y segundos, calcular cuantos segundos han transcurrido desde el comiendo del día

hora = 0
minutos = 0
seg = 0

hora = int(input("Intoduzca la hora: "))
minutos = int(input("Intoduzca los minutos: "))
seg = int(input("Intoduzca los segundos: "))

hora = hora * 3600
minutos= minutos * 60
seg= seg + minutos + hora

print("el total de segundos transcurridos desde el comienzo del día son: ", seg, "segundos")


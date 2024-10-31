#edad
from time import localtime

# Obtener la fecha actual
t = localtime()
dia_actual = t.tm_mday
mes_actual = t.tm_mon
anno_actual = t.tm_year

# Solicitar al usuario que ingrese su fecha de nacimiento
print("Ingrese su fecha de nacimiento.")
dia_nacimiento = int(input("Día: "))
mes_nacimiento = int(input("Mes: "))
anno_nacimiento = int(input("Año: "))

# Calcular la edad
edad = anno_actual - anno_nacimiento

# Ajustar la edad si el cumpleaños no ha ocurrido aún este año
if (mes_nacimiento > mes_actual) or (mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
    edad -= 1

# Mostrar la edad del usuario
print(f"Usted tiene {edad} años.")
#Palabra más larga
# Solicitar al usuario que ingrese dos palabras
palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")

# Calcular la longitud de las palabras
longitud1 = len(palabra1)
longitud2 = len(palabra2)

# Comparar las longitudes y determinar el resultado
if longitud1 > longitud2:
    diferencia = longitud1 - longitud2
    print(f"La palabra {palabra1} tiene {diferencia} letras más que {palabra2}.")
elif longitud2 > longitud1:
    diferencia = longitud2 - longitud1
    print(f"La palabra {palabra2} tiene {diferencia} letras más que {palabra1}.")
else:
    print("Las dos palabras tienen el mismo largo.")
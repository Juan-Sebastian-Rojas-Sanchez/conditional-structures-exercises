#Letra o numero
# Solicitar al usuario que ingrese un carácter
caracter = input("Ingrese caracter: ")

# Verificar si es una letra
if caracter.isalpha():
    if caracter.isupper():
        print("Es letra mayúscula.")
    else:
        print("Es letra minúscula.")
# Verificar si es un número
elif caracter.isdigit():
    print("Es número.")
# Si no es ni letra ni número
else:
    print("No es letra ni número.")
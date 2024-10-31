#triangulos
def tipo_triangulo(a, b, c):
    # Verificar si es un triángulo válido
    if a + b > c and a + c > b and b + c > a:
        # Determinar el tipo de triángulo
        if a == b == c:
            return "El triángulo es equilátero."
        elif a == b or a == c or b == c:
            return "El triángulo es isósceles."
        else:
            return "El triángulo es escaleno."
    else:
        return "No es un triángulo válido."

# Ciclo para permitir múltiples entradas
while True:
    try:
        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
        
        # Verificar el tipo de triángulo
        resultado = tipo_triangulo(a, b, c)
        print(resultado)
        
    except ValueError:
        print("Error: Ingrese un número válido.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea verificar otro triángulo? (s/n): ")
    if continuar.lower() != 's':
        break
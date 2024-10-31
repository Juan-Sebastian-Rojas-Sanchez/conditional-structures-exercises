#calculadora
# Función para realizar la operación
def calcular(operando1, operador, operando2):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 != 0:
            return operando1 / operando2
        else:
            return "Error: División por cero."
    elif operador == '**':
        return operando1 ** operando2
    else:
        return "Operador no válido."

# Ciclo para permitir múltiples operaciones
while True:
    # Solicitar al usuario que ingrese un operando, operador y segundo operando
    try:
        operando1 = float(input("Operando: "))
        operador = input("Operador: ")
        operando2 = float(input("Operando: "))

        # Calcular el resultado
        resultado = calcular(operando1, operador, operando2)

        # Mostrar el resultado
        print(f"{operando1} {operador} {operando2} = {resultado}")
    except ValueError:
        print("Error: Entrada no válida. Asegúrese de ingresar números reales.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break
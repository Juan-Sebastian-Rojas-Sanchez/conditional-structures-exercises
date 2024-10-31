#set de tenis
def verificar_set(juegos_a, juegos_b):
    # Comprobar si el resultado es inválido
    if (juegos_a >= 7 and juegos_b >= 6) or (juegos_b >= 7 and juegos_a >= 6):
        print("Invalido")
    # Comprobar si A ganó el set
    elif juegos_a >= 6 and juegos_a - juegos_b >= 2:
        print("Gano A")
    # Comprobar si B ganó el set
    elif juegos_b >= 6 and juegos_b - juegos_a >= 2:
        print("Gano B")
    # Comprobar si el set está empatado a 5
    elif juegos_a == 5 and juegos_b == 5:
        print("Aun no termina")
    # Comprobar si el set está empatado a 6
    elif juegos_a == 6 and juegos_b == 6:
        print("Aun no termina")
    # Si el set todavía no ha terminado
    elif juegos_a < 6 and juegos_b < 6:
        print("Aun no termina")
    else:
        print("Invalido")

# Ciclo para permitir múltiples entradas
while True:
    try:
        juegos_a = int(input("Juegos ganados por A: "))
        juegos_b = int(input("Juegos ganados por B: "))
        
        # Verificar el estado del set
        verificar_set(juegos_a, juegos_b)
        
    except ValueError:
        print("Error: Ingrese un número entero válido.")
    
    # Preguntar si desea continuar
    continuar = input("¿Desea verificar otro set? (s/n): ")
    if continuar.lower() != 's':
        break
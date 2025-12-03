def es_numero_perfecto(n: int) -> bool:
    """Retorna True si n es un número perfecto, de lo contrario False."""
    if n <= 1:
        return False
    
    suma_divisores = 1  # 1 siempre es divisor (para n > 1)

    # Solo revisamos hasta la raíz cuadrada para mejor eficiencia
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma_divisores += i
            otro = n // i
            if otro != i:     # evitar duplicar divisores cuadrados
                suma_divisores += otro

    return suma_divisores == n
def pedir_numero_perfecto():
    """Interfaz sencilla por consola para solicitar un entero y verificar si es perfecto.

    El usuario puede escribir 'b' o 'salir' para volver al menú principal.
    """
    while True:
        entrada = input("Ingrese un entero positivo (o 'b' para volver): ")
        if entrada.lower() in {"b", "salir", "q", "exit"}:
            break
        try:
            n = int(entrada)
            if n < 1:
                raise ValueError
            if es_numero_perfecto(n):
                print(f"{n} es un número perfecto.")
            else:
                print(f"{n} no es un número perfecto.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un entero positivo.")
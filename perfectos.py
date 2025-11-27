def es_perfecto(numero):
    """
    Determina si un número es perfecto.
    Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos.
    Ejemplo: 6 = 1 + 2 + 3
    """
    if numero < 1:
        return False
    
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    
    return suma_divisores == numero


def numeros_perfectos(n):
    """
    Genera los primeros N números perfectos.
    Nota: Los números perfectos son muy raros, solo existen 51 conocidos.
    """
    if n <= 0:
        return []
    
    perfectos = []
    numero_actual = 1
    
    # Límite de búsqueda para evitar esperas muy largas
    # Los primeros números perfectos son: 6, 28, 496, 8128
    while len(perfectos) < n and numero_actual < 10000:
        if es_perfecto(numero_actual):
            perfectos.append(numero_actual)
        numero_actual += 1
    
    return perfectos


def mostrar_perfectos():
    """
    Función principal para interactuar con el usuario.
    """
    print("\n=== NÚMEROS PERFECTOS ===")
    try:
        n = int(input("¿Cuántos números perfectos deseas generar? (máx 4): "))
        
        if n <= 0:
            print("Por favor ingresa un número positivo.")
            return
        
        if n > 4:
            print("Advertencia: Solo se buscarán los primeros 4 números perfectos.")
            n = 4
        
        print(f"\nBuscando los primeros {n} números perfectos...")
        perfectos = numeros_perfectos(n)
        
        if perfectos:
            print(f"\nLos primeros {len(perfectos)} números perfectos son:")
            for i, num in enumerate(perfectos, 1):
                # Mostrar los divisores del número perfecto
                divisores = [str(j) for j in range(1, num) if num % j == 0]
                print(f"{i}. {num} = {' + '.join(divisores)}")
        else:
            print("No se encontraron números perfectos en el rango buscado.")
            
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")


# Código de prueba (puedes comentarlo después)
if __name__ == "__main__":
    mostrar_perfectos()
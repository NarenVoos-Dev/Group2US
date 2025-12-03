from fibonacci import fibonacci
from factoriales import pedir_factorial
from primes import pedir_primo
from Suma import suma
from NumerosPerfectos import pedir_numero_perfecto

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Número primo")
        print("4. N números perfectos")
        print("5. Sumar dos numeros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fibonacci()

        elif opcion == "2":
            pedir_factorial()
           
        elif opcion == "3":
            pedir_primo()

        elif opcion == "4":
            pedir_numero_perfecto()

        elif opcion == "5":
           # Pedir dos números al usuario y mostrar la suma
           a = input("Ingrese el primer número: ")
           b = input("Ingrese el segundo número: ")
           try:
               resultado = suma(a, b)
               print(f"Resultado de la suma: {resultado}")
           except Exception as e:
               print("Error al sumar:", e)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

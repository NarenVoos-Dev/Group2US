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
            print(f"Fibonacci")

        elif opcion == "2":
            print(f"Factorial")
           
        elif opcion == "3":
            print(f"Número primo")

        elif opcion == "4":
           print(f" N números perfectos")

        elif opcion == "5":
           print(f" Suma dos numeros")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

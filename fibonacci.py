def fibonacci():

    numero_uno, numero_dos = 0, 1

    while numero_uno <= 1597:
        print(numero_uno, end=' ')
        numero_uno, numero_dos = numero_dos, numero_uno + numero_dos

    print('fin\n')

if __name__ == "__main__":
    
    fibonacci()
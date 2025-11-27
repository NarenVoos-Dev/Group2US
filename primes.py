"""Módulo para operaciones con números primos.

Provee:
- es_primo(n): determina si n es primo (bool).
- pedir_primo(): interfaz por consola para consultar números primos.
"""
from math import isqrt
from typing import List


def es_primo(n: int) -> bool:
    """Devuelve True si n es primo, False en caso contrario.

    Solo acepta enteros; para n < 2 devuelve False.
    Implementación eficiente: prueba 2 y luego impares hasta sqrt(n).
    """
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def listar_primos_hasta(n: int) -> List[int]:
    """Devuelve la lista de primos <= n usando la criba de Eratóstenes.

    Para n < 2 devuelve lista vacía.
    """
    if not isinstance(n, int) or n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"  # 0 y 1 no son primos
    limit = isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def pedir_primo():
    """Interfaz por consola: pide un entero y muestra si es primo.

    Comandos disponibles:
    - 'b' o 'salir' para volver al menú principal.
    - Si la entrada es un entero positivo n, se muestra si n es primo y,
      además, se ofrece listar todos los primos <= n si el usuario lo desea.
    """
    while True:
        entrada = input("Ingrese un entero para verificar primo (o 'b' para volver): ")
        if entrada.lower() in {"b", "salir", "q", "exit"}:
            break
        try:
            n = int(entrada)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un entero.")
            continue

        if es_primo(n):
            print(f"{n} es primo.")
        else:
            print(f"{n} NO es primo.")

        # Ofrecer listar primos hasta n si n > 1
        if n > 1:
            ver = input("¿Desea listar todos los primos <= {0}? (s/n): ".format(n))
            if ver.lower() in {"s", "si", "y", "yes"}:
                primos = listar_primos_hasta(n)
                print("Primos <= {0}: {1}".format(n, ", ".join(map(str, primos))))


if __name__ == "__main__":
    pedir_primo()

"""Módulo de factoriales.

Provee:
- factorial(n): devuelve n! para enteros no negativos.
- pedir_factorial(): wrapper CLI para pedir un número y mostrar el factorial.
"""

def factorial(n: int) -> int:
	"""Calcula el factorial de n.

	Args:
		n (int): entero no negativo

	Returns:
		int: n!

	Raises:
		ValueError: si n no es un entero o es negativo.
	"""
	if not isinstance(n, int):
		raise ValueError("n debe ser un entero no negativo")
	if n < 0:
		raise ValueError("n debe ser un entero no negativo")

	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


def pedir_factorial():
	"""Interfaz sencilla por consola para solicitar un entero y mostrar su factorial.

	El usuario puede escribir 'b' o 'salir' para volver al menú principal.
	"""
	while True:
		entrada = input("Ingrese un entero no negativo (o 'b' para volver): ")
		if entrada.lower() in {"b", "salir", "q", "exit"}:
			break
		try:
			n = int(entrada)
			print(f"{n}! = {factorial(n)}")
		except ValueError as e:
			print("Entrada inválida. Por favor ingrese un entero no negativo.")


if __name__ == "__main__":
	pedir_factorial()


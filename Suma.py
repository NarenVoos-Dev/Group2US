"""Módulo Suma

Provee una función `suma(a, b)` que devuelve la suma de dos valores numéricos.
Acepta ints, floats o cadenas numéricas (por ejemplo "3" o "2.5").
"""

from typing import Union


NumberLike = Union[int, float, str]


def suma(a: NumberLike, b: NumberLike) -> Union[int, float]:
	"""Devuelve la suma de `a` y `b`.

	- Si ambos argumentos son enteros se devuelve un int.
	- Si alguno es float o una cadena numérica con decimales, se devuelve float.
	- Si los valores no son convertibles a número se lanza TypeError.

	Examples
	--------
	>>> suma(2, 3)
	5
	>>> suma("1.5", 2)
	3.5
	"""
	# Intentar suma directa para tipos numéricos ya convertidos
	try:
		result = a + b  # type: ignore
		# si no lanza TypeError, tratar de devolver int cuando corresponda
		if isinstance(result, float) and float(result).is_integer():
			return int(result)
		return result
	except TypeError:
		# Intentar convertir a float desde cadenas u otros tipos
		try:
			a_num = float(a)
			b_num = float(b)
		except Exception:
			raise TypeError("Los valores deben ser números o cadenas numéricas")

		suma_float = a_num + b_num
		# devolver int si la suma es entera
		if suma_float.is_integer():
			return int(suma_float)
		return suma_float


if __name__ == "__main__":
	# Demo rápido cuando se ejecuta el módulo directamente
	try:
		a = input("Ingrese el primer número: ")
		b = input("Ingrese el segundo número: ")
		print("Resultado:", suma(a, b))
	except Exception as e:
		print("Error:", e)

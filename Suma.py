from typing import Union

NumberLike = Union[int, float, str]

def suma(a: NumberLike, b: NumberLike) -> Union[int, float]:
    """Devuelve la suma de `a` y `b`."""
    # Convertir todo a número primero
    try:
        a_num = float(a)
        b_num = float(b)
    except Exception:
        raise TypeError("Los valores deben ser números o cadenas numéricas")

    resultado = a_num + b_num

    # Si el resultado es entero exacto → devolver int
    if resultado.is_integer():
        return int(resultado)
    return resultado

if __name__ == "__main__":
    try:
        a = input("Ingrese el primer número: ")
        b = input("Ingrese el segundo número: ")
        c = suma(a, b)
        print("Resultado:", c)
    except Exception as e:
        print("Error:", e)

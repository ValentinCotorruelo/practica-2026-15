"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve True si se lee igual al derecho y al revés,
    False en caso contrario. Usa slices de listas."""
    return palabra == palabra[::-1]


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Devuelve la mitad de un string. Si es impar, redondea hacia arriba sin usar math."""
    longitud = len(palabra)
    # División entera + ajuste para impar
    indice_mitad = (longitud // 2) + (longitud % 2)
    return palabra[:indice_mitad]


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN

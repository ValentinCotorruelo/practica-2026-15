"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    letra = letra.lower()
    
    if letra == "a":
        return True
    if letra == "e":
        return True
    if letra == "i":
        return True
    if letra == "o":
        return True
    if letra == "u":
        return True
    
    return False


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    if letra.lower() in "aeiou":
        return True
    return False

# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    return letra.lower() in "aeiou"


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN

# ultimo_digito.py
# Último dígito.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    ultimoDigito :: Int -> Int
# tal que (ultimoDigito x) es el último dígito del número x. Por
# ejemplo,
#    ultimoDigito(325) == 5
# ---------------------------------------------------------------------


def ultimoDigito(x):
    # type: (int) -> int
    return x % 10

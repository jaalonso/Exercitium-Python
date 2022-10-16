# base_de_dato_de_actividades.py
# Base de dato de actividades.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las bases de datos sobre actividades de personas pueden representarse
# mediante listas de elementos de la forma (a,b,c,d), donde a es el
# nombre de la persona, b su actividad, c su fecha de nacimiento y d la
# de su fallecimiento. Un ejemplo es la siguiente que usaremos a lo
# largo de este ejercicio,
#    BD = list[tuple[str, str, int, int]]
#
#    personas: BD = [
#        ("Cervantes", "Literatura", 1547, 1616),
#        ("Velazquez", "Pintura", 1599, 1660),
#        ("Picasso", "Pintura", 1881, 1973),
#        ("Beethoven", "Musica", 1770, 1823),
#        ("Poincare", "Ciencia", 1854, 1912),
#        ("Quevedo", "Literatura", 1580, 1654),
#        ("Goya", "Pintura", 1746, 1828),
#        ("Einstein", "Ciencia", 1879, 1955),
#        ("Mozart", "Musica", 1756, 1791),
#        ("Botticelli", "Pintura", 1445, 1510),
#        ("Borromini", "Arquitectura", 1599, 1667),
#        ("Bach", "Musica", 1685, 1750)]
#
# Definir las funciones
#    nombres   : (BD) -> list[str]
#    musicos   : (BD) -> list[str]
#    seleccion : (BD, str) -> list[str]
#    musicos2  : (BD) -> list[str]
#    vivas     : (BD, int) -> list[str]
# tales que
# + nombres(bd) es la lista de los nombres de las personas de la- base
#   de datos bd. Por ejemplo,
#      >>> nombres(personas)
#      ['Cervantes','Velazquez','Picasso','Beethoven','Poincare',
#       'Quevedo','Goya','Einstein','Mozart','Botticelli','Borromini',
#       'Bach']
# + musicos(bd) es la lista de los nombres de los músicos de la base
#   de datos bd. Por ejemplo,
#      musicos(personas)  ==  ['Beethoven','Mozart','Bach']
# + seleccion(bd, m) es la lista de los nombres de las personas de la
#   base de datos bd cuya actividad es m. Por ejemplo,
#      >>> seleccion(personas, 'Pintura')
#      ['Velazquez', 'Picasso', 'Goya', 'Botticelli']
#      >>> seleccion(personas, 'Musica')
#      ['Beethoven', 'Mozart', 'Bach']
# + musicos2(bd) es la lista de los nombres de los músicos de la base
#   de datos bd. Por ejemplo,
#      musicos2(personas)  ==  ['Beethoven','Mozart','Bach']
# + vivas(bd, a) es la lista de los nombres de las personas de la base
#   de datos bd  que estaban vivas en el año a. Por ejemplo,
#      >>> vivas(personas, 1600)
#      ['Cervantes', 'Velazquez', 'Quevedo', 'Borromini']
# ---------------------------------------------------------------------

BD = list[tuple[str, str, int, int]]

personas: BD = [
    ("Cervantes", "Literatura", 1547, 1616),
    ("Velazquez", "Pintura", 1599, 1660),
    ("Picasso", "Pintura", 1881, 1973),
    ("Beethoven", "Musica", 1770, 1823),
    ("Poincare", "Ciencia", 1854, 1912),
    ("Quevedo", "Literatura", 1580, 1654),
    ("Goya", "Pintura", 1746, 1828),
    ("Einstein", "Ciencia", 1879, 1955),
    ("Mozart", "Musica", 1756, 1791),
    ("Botticelli", "Pintura", 1445, 1510),
    ("Borromini", "Arquitectura", 1599, 1667),
    ("Bach", "Musica", 1685, 1750)]

def nombres(bd: BD) -> list[str]:
    return [p[0] for p in bd]

def musicos(bd: BD) -> list[str]:
    return [p[0] for p in bd if p[1] == "Musica"]

def seleccion(bd: BD, m: str) -> list[str]:
    return [p[0] for p in bd if p[1] == m]

def musicos2(bd: BD) -> list[str]:
    return seleccion(bd, "Musica")

def vivas(bd: BD, a: int) -> list[str]:
    return [p[0] for p in bd if p[2] <= a <= p[3]]

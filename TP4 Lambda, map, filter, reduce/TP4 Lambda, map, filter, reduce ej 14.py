# 14.Crea una función masCorto que acepte una lista de strings como argumento y devuelva el string más corto de la lista.
# Utiliza la función reduce y una función lambda para implementarla.

from functools import reduce

lista = ["Sol","Luna","Estrellas"]

def mas_corto(lista):
    return reduce(lambda a,b : a if len(a) < len(b) else b, lista)

print(mas_corto(lista))
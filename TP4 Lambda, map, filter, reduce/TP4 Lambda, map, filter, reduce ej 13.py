# 13.Crea una función productoPares que acepte una lista de números como argumento y devuelva el producto de todos los
# números pares de la lista. Utiliza la función reduce y una función lambda para implementarla.

from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]

pares = list(filter(lambda lista : lista if lista % 2 == 0 else None,lista))
# print(pares)

productoPares = reduce(lambda a,b : a*b,pares)

print(productoPares)
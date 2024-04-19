# 11.Crea una función esDivisible que acepte un número como argumento, y una lista de números, y devuelva una nueva lista con los
# números de la lista que son divisibles por el número dado. Utiliza funciones lambda y filter para implementarla.

lista = [1,2,3,9,10,12,7,30,27]
num = 3

esDivisible = lambda num, lista : list(filter(lambda lista : lista if lista % num == 0 else None,lista))

print(esDivisible(num,lista))


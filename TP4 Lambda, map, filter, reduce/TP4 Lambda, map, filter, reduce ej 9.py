# 9.Crea una función filtraMayores que acepte una lista de números como argumento y devuelva una nueva lista con los números
# mayores que 5. Utiliza la función filter para implementarla.

lista = [1,2,3,4,5,6,7,8,9,10]

filtraMayores = list(filter(lambda lista : lista if lista > 5 else None, lista))

print(filtraMayores)
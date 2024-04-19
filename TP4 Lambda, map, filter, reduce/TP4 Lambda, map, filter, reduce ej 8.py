# 8.Crea una función doble que acepte una lista de números como argumento y devuelva una nueva lista con cada número
# multiplicado por dos. Utiliza la función map para implementarla.

listx = [1,2,3,4,5,6,7,8,9,10]

lista_multiplicada = lambda lista : list(map(lambda lista : lista * 2, listx))

print("Lista multiplicada por 2: ",lista_multiplicada(listx))
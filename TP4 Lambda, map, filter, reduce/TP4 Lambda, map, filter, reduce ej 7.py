# 7.Escriba un programa que utilizando map y una función lambda como argumento, permita generar una nueva lista con el
# resultado de la división en 1 (es decir, 1/x) de cada elemento de la lista

lista = [1,2,3,4,5,6,7,8,9,10]

nueva_lista = list(map(lambda lista : 1 / lista, lista))

print("Resultado de 1 dividido por cada valor de la lista: ",nueva_lista)
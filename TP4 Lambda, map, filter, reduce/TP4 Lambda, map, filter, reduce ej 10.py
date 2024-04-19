# 10.Crea una función dobleSiEsPar que acepte una lista de números como argumento, devuelva una nueva lista con cada número
# multiplicado por dos si es par, y elimine todos los números impares de la lista. Utiliza funciones lambda, map y filter para
# implementarla.

def filtrado(listx):
    return list(filter(lambda lista : lista if lista % 2 == 0 else None,listx))

def main():
    listx = [1,2,3,4,5,6,7,8,9,10]
    filtrado_pares = filtrado(listx)
    dobleSiEsPar = list(map(lambda lista : lista * 2, filtrado_pares))
    print("Lista original: ",listx)
    print("Nueva lista: ",dobleSiEsPar)
    
main()
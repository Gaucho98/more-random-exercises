# 5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma
# ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
# Desarrollar además un programa para verificar el comportamiento de la función.

def funcion(lista):
    if lista[0] < lista[-1]:
        return True
    elif lista[0] > lista[-1]:
        return False

def main():
    lista = [1,2,3] """[3,2,1] ["a","b"] ["b","a"]"""
    msj = funcion(lista)
    print(msj)
    
main()
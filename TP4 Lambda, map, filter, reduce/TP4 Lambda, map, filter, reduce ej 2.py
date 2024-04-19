# 2. Escriba un programa para generar una función (utilizando filter) y lambdas para separar los números pares e impares de
# una lista de números. La función debe retornar dos valores resultantes.

def funcion(lista):
    filter_pares = list(filter(lambda numero : numero % 2 == 0,lista))
    filter_impares = list(filter(lambda numero : numero % 2 == 1,lista))
    
    return filter_pares,filter_impares

def main():
    lista = [1,2,3,4,5,6,7,8,9]
    lista_pares,lista_impares = funcion(lista)
    print(lista_pares)
    print(lista_impares)
    
main()
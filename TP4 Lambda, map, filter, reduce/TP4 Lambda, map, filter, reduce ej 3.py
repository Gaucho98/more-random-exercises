# 3. Escriba un programa para contar los números pares e impares en una lista dada de enteros usando Lambda.

def cantidad_par_impar(lista):
    lista_pares = list(filter(lambda numero : numero % 2 == 0,lista))
    lista_impares = list(filter(lambda numero : numero % 2 == 1,lista))
    
    pares = len(lista_pares)
    impares = len(lista_impares)
    
    return pares,impares
    
def main():
    lista = [1,2,3,4,5,6,7,8,9]
    pares,impares = cantidad_par_impar(lista)
    print("Cantidad de pares: ",pares)
    print("Cantidad de impares: ",impares)
    
main()
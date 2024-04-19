# 9.Generar una lista con 50 números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que
# sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.

import random

def generacion_de_listas():
    lista = [random.randint(1,100) for i in range(50)]
    lista_impares = [lista[i] for i in range(len(lista)) if lista[i] % 2 == 1]
    
    return lista,lista_impares

def main():
    lista,lista_impares = generacion_de_listas()
    print("Lista original: ",lista)
    print("Lista de impares de la lista original: ",lista_impares)
    
main()
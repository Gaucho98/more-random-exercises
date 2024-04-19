# 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo
# la lista luego de invocar a cada función:
# a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos
# dígitos. Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
# b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
# c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la
# función lo recibe como parámetro. Utilice comprensión de listas para resolverlo.
# d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares.
# Un ejemplo de lista capicúa es [50,17,91,17,50].

import random

def list_gen():
    lista = []
    n = random.randint(1,10)
    
    for i in range(n):
        valor = random.randint(1000,9999)
        lista.append(valor)
        
    lista_comprension = [random.randint(1000,9999) for i in range(n)]
        
    return lista, lista_comprension

def sumatoria_lista(l_c):
    sumatoria = sum(l_c)
    
    return sumatoria

def eliminacion_valor(l_c):
    lista2 = []
    
    numero_eliminar = int(input("Ingrese un numero del 1000 al 9999: "))
    while numero_eliminar < 1000 or numero_eliminar > 9999:
        numero_eliminar = int(input("El numero ingresado esta fuera de rango, intente nuevamente"))
        
    lista3 = [l_c[i] for i in range(len(l_c)) if numero_eliminar != l_c[i]]
            
    return lista2,lista3

def capicua():
    lista = [50,17,91,17,50]
    
    lista2 = lista[::-1]
    
    if lista == lista2:
        print("Lista: ",lista,"--> La lista es capicua.")
    elif lista != lista2:
        print("Lista: ",lista,"--> La lista no es capicua.")
    
def main():
    lista, l_c = list_gen()
    print("Lista: ",lista)
    print("Lista por comprension:", l_c)
    sumatoria = sumatoria_lista(l_c)
    print("Suma de los elementos de la lista: ", sumatoria)
    lista2,lista3 = eliminacion_valor(l_c)
    print("Lista con valor ingresado eliminado: ", lista3)
    capicua()
        
main()
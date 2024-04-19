# 3.Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
# Luego se solicita imprimir los últimos 10 valores de la lista utilizando segmentación de listas.

import random

def crear_lista(n):
#     lista = []
#      
#     for i in range(n):
#         valor = random.randint(1,n)
#         lista.append(valor ** 2)
    
    lista = [(random.randint(1,n)**2) for i in range(n)]
    
    return lista

def ultimos_10_valores(lista):
    print("Ultimos 10 valores de la lista: ", lista[-10::])
    
def main():
    n = int(input("Ingrese N: "))
    lista = crear_lista(n)
    print("Lista generada con los cuadrados:", lista)
    ultimos_10_valores(lista)
    
main()
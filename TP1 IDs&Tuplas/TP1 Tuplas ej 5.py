# Suma de números: crea un programa que lea una lista de tuplas, donde cada tupla contiene dos números enteros, y calcule
# la suma de los números en cada tupla. Por ejemplo, si llamamos a la función con la lista de tuplas [(1, 2), (3, 4), (5, 6)],
# la función devolverá el valor 21, que es la suma de los números en todas las tuplas.

import random

def lista_tuplas():
    num = random.randint(1,9)
    lista_tuplas = []
    
    for i in range(num):
        x = random.randint(0,9)
        y = random.randint(0,9)
        tupla = (x,y)
        lista_tuplas.append(tupla)
        
    return lista_tuplas

def suma(tuple_list):
    suma_tupla = []
    acumulador = 0
    
    for i,j in tuple_list:
        suma = i + j
        suma_tupla.append(suma)
        
    for i in range(len(suma_tupla)):
        acumulador += suma_tupla[i]
        
    return acumulador
        
def main():
    tuple_list = lista_tuplas()
    print(tuple_list)
    acu = suma(tuple_list)
    print("Suma =", acu)
    
main()
# Escribir funciones para:
# a.Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión de listas para generar el resultado.
# b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe
# modificar la lista.
# c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar
# el orden. Combinar estas tres funciones en un mismo programa.

import random

def lista_aleatoria():
    lista = [random.randint(1,100) for i in range(50)]
    return lista

def elemento_repetido(lista):
    
    for i in range(len(lista)):
        n = lista.count(lista[i])
#         print(n)
        if n > 1:
            return True
        
def lista_sin_repetidos(lista):
    lista2 = []
    
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2.append(lista[i])
            
    return lista2
            
def main():
    lista = lista_aleatoria()
    print("Lista generada con el metodo comprension de listas: ", lista)
    c = elemento_repetido(lista)
    print("Elemento repetido? ", c)
    lista2 = lista_sin_repetidos(lista)
    print("Lista sin numeros repetidos: ", lista2)
    
main()
# Suma de Matrices: escribir una función que reciba dos matrices como entrada y devuelva la matriz resultante de su suma.
# Se asume que ambas matrices tienen las mismas dimensiones.

import random

def carga_matriz(dimension):
    matriz = []
    
    for i in range(dimension):
        matriz.append([])
        for j in range(dimension):
            valor = random.randint(0,9)
            matriz[i].append(valor)
    return matriz

def impresion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def suma_matrices(matriz1,matriz2):
    matriz_suma = []
    
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        matriz_suma.append(fila)
    return matriz_suma
            
def main():
    dimension = int(input("Ingrese la dimension de la matriz: "))
    matriz1 = carga_matriz(dimension)
    matriz2 = carga_matriz(dimension)
    print("Matriz 1: ")
    impresion(matriz1)
    print("Matriz 2: ")
    impresion(matriz2)
    matriz_suma = suma_matrices(matriz1,matriz2)
    print("Suma matrices: ")
    impresion(matriz_suma)
    
main()
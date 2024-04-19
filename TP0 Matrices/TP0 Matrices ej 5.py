# Suma de Filas y Columnas: crear una función que tome una matriz como entrada y devuelva una lista con la suma de cada fila
# y otra lista con la suma de cada columna

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
        
def suma_filas(matriz):
    lista_suma_filas = []
    sumador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sumador += matriz[i][j]
        lista_suma_filas.append(sumador)
        sumador = 0
    return lista_suma_filas
        
def suma_columnas(matriz):
    lista_suma_columnas = []
    sumador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sumador += matriz[j][i]
        lista_suma_columnas.append(sumador)
        sumador = 0
    return lista_suma_columnas
        
def main():
    dimension = int(input("Ingrese la dimension de la matriz: "))
    matriz = carga_matriz(dimension)
    impresion(matriz)
    filas_sumadas = suma_filas(matriz)
    print("Lista suma de filas: ", filas_sumadas)
    columnas_sumadas = suma_columnas(matriz)
    print("Lista suma de columnas: ", columnas_sumadas)

main()
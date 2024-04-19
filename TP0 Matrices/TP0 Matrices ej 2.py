# Crea una matriz con un tamaño que el usuario le indique por teclado (puede ser 6×4, 7×2, etc.) pero como máximo podrá
# contener 10x10 valores y como mínimo 2x2. Crear una función para la cargar de los valores y, por último, otro procedimiento
# para visualizar los resultados. Los valores para cargar deberán ser número positivos entre 0 y 100, siendo éstos generados
# al azar.

import random

def carga_matriz(fila,columna):
    matriz = []
    
    for i in range(fila):
        matriz.append([])
        for j in range(columna):
            valor = random.randint(0,100)
            matriz[i].append(valor)
    return matriz

def impresion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")

def main():
    fila = int(input("Indique la cantidad de filas: "))
    while fila < 2 or fila > 10:
        fila = int(input("Solo se permite un maximo de filas de 10 y un minimo de 2. Intente nuevamente: "))
    columna = int(input("Indique la cantidad de columnas: "))
    while columna < 2 or columna > 10:
        columna = int(input("Solo se permite un maximo de columnas de 10 y un minimo de 2. Intente nuevamente: "))
    matriz = carga_matriz(fila,columna)
    impresion(matriz)
    
main()
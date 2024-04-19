# Producto Escalar: crear una función que tome una matriz y un número como entrada, y devuelva la matriz resultante de
# multiplicar cada elemento por el número dado.

import random

def carga_matriz(f,c):
    matriz = []
    
    for i in range(f):
        matriz.append([])
        for j in range(c):
            valor = random.randint(0,9)
            matriz[i].append(valor)
    return matriz

def impresion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def matriz_multiplicada(matriz,numero):
    matriz_mult = []
    
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            multiplicacion = matriz[i][j] * numero
            fila.append(multiplicacion)
        matriz_mult.append(fila)
    return matriz_mult
            
def main():
    f = int(input("Ingrese la cantidad de filas: "))
    c = int(input("Ingrese la cantidad de columnas: "))
    matriz = carga_matriz(f,c)
    print("Matriz: ")
    impresion(matriz)
    numero = int(input("Ingrese un numero, el cual se tomara para multiplicar cada elemento de la matriz: "))
    matriz_mult = matriz_multiplicada(matriz,numero)
    print("Matriz multiplicada por", numero,": ")
    impresion(matriz_mult)
    
main()
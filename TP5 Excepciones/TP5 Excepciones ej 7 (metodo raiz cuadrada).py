# 7. Escribe una función llamada calcularRaizCuadrada que reciba un número como argumento y calcule su raíz cuadrada.
# Si el número es negativo, la función debe generar una excepción ValueError con un mensaje indicando que no se puede
# calcular la raíz cuadrada de un número negativo.

import math

def calcularRaizCuadrada(num):
    try:
        raiz_cua = math.sqrt(num)
        print(raiz_cua)
    except:
        print("No se puede calcular la raíz cuadrada de un número negativo.")

def main():
    num = int(input("Ingrese un numero: "))
    calcularRaizCuadrada(num)
    
main()

# metodo para calcular raiz cuadrada:
# import math
# variable = math.sqrt(num)
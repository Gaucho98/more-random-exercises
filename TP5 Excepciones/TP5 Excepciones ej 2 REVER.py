# 2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos
# valores y devuelva el resultado como un número real. Devolver None si alguna de las cadenas no contiene un número válido,
# utilizando manejo de excepciones para detectar el error.

def funcion_suma(n1,n2):
    try:
        suma = int(n1) + int(n2)
        return suma
    except:
        return None

def main():
    n1 = input("Ingrese un numero: ")
    n2 = input("Ingrese otro numero: ")
    suma = funcion_suma(n1,n2)
    print(suma)
    
main()
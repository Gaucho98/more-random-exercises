# 1. Desarrollar una función para ingresar a través del teclado un número. La función rechazará cualquier ingreso
# inválido de datos utilizando excepciones y mostrará la razón exacta del error. Devolver el valor ingresado cuando éste
# sea correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.

def funcion():
    flag = False
    
    while flag == False:
        try:
            numero = int(input("Ingrese un numero: "))
#             flag = True
#             return numero
        except ValueError:
            flag = False
            print("El valor ingresado no es un entero.")
        else:
            flag = True
            return numero

def main():
    numero = funcion()
    print("Resultado: ", numero)
    
main()
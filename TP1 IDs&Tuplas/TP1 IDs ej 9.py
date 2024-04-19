#  Crear una función que reciba dos números enteros como parámetros. Ambos valores recibidos como parámetros se deben modificar.
#  Imprimir los IDs de ambos números antes, durante y después de la llamada a la función.
#  ¿Cuál es la relación entre los IDs antes y después de la llamada a la función?

def funcion(numero1,numero2):
    numero1 = 3
    numero2 = 4
    
    print("ID 1 en-funcion: ", id(numero1))
    print("ID 2 en-funcion: ", id(numero2))
    
    return numero1,numero2
    
def main():
    numero1 = 1
    numero2 = 2
    print("ID 1 pre-funcion: ", id(numero1))
    print("ID 2 pre-funcion: ", id(numero2))
    num1,num2 = funcion(numero1,numero2)
    print("ID 1 post-funcion: ", id(num1))
    print("ID 2 post-funcion: ", id(num2))
    
main()
# 7.Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada. La cadena y el valor
# de N se pasan como parámetros.

def funcion(cadena,n):
    subcadena = cadena[-n::]
    return subcadena
    
def main():
    cadena = "La calesita gira rapido"
    n = int(input("Ingrese N: "))
    subcadena = funcion(cadena,n)
    print(subcadena)
    
main()
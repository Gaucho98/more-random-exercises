# 1. Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.

def cant_dig(num):
    if num < 10:
        return 1
    elif num > 10:
        return 1 + cant_dig(num//10)    
    
def main():
    print(cant_dig(878787))

main()

print(99//10)
# 5. Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar entre
# 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el
# número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe imprimir en pantalla
# la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número se mostrará un
# mensaje en pantalla y se lo contará como un intento más.

import random

def juego():
    num_secreto = random.randint(1,10)
    intentos = 0
    
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            intentos += 1
            
            if num > num_secreto:
                print("El numero es MENOR")
            elif num < num_secreto:
                print("El numero es MAYOR")
            elif num == num_secreto:
                return(f"Encontraste el numero! \nCantidad de intentos: {intentos}")
        except:
            print("El valor ingresado no es un numero, intente nuevamente.")
            intentos += 1
            
def main():
    print("Adivine el numero secreto!")
    msj = juego()
    print(msj)
    
main()
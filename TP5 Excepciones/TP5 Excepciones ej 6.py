# 6. Convertir una cadena en un número: Escribe un programa que solicite al usuario una cadena y luego intente convertirla
# en un número entero. Si la conversión falla, muestra un mensaje de error.

def convertir_cadena():
    try:
        cadena = input("Ingrese una cadena: ")
        cadenaAentero = int(cadena)
        print(cadenaAentero)
    except ValueError:
        print("La conversion ha fallado.")
    
def main():
    convertir_cadena()
    
main()
# 11. Capitalizar la primera letra: Crea un programa que le pida al usuario que ingrese una cadena y luego capitalice
# la primera letra de cada palabra en la cadena. Puedes usar el método title() para hacer esto.

def capitalizar_cadena(cadena):
    return cadena.title()

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    cadena_capitalizada = capitalizar_cadena(cadena)
    print(cadena_capitalizada)
    
main()
# 10.Eliminar caracteres: Crea un programa que le pida al usuario que ingrese una cadena y luego elimine todas las
# ocurrencias de un carácter específico en la cadena. Por ejemplo, puedes pedirle al usuario que ingrese una cadena y
# luego eliminar todas las letras "a".

def eliminar_caracteres(cadena,char_eliminar):
    lista_cadena = []
    
    for i in range(len(cadena)):
        if cadena[i] != char_eliminar:
            lista_cadena.append(cadena[i])
            
    nueva_cadena = "".join(lista_cadena)
    
    return nueva_cadena

def main():
    cadena = input("Ingrese una cadena: ")
    char_eliminar = input("Ingrese un caracter a eliminar: ")
    nueva_cadena = eliminar_caracteres(cadena,char_eliminar)
    print("Cadena ingresada: ", cadena)
    print("Cadena modificada: ", nueva_cadena)
    
main()
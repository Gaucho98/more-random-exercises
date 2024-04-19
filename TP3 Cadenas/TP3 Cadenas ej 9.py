# 9.Contar el número de vocales: Crea un programa que le pida al usuario que ingrese una cadena y luego cuente y muestre
# el número de vocales que hay en la cadena. Ayuda: Puedes usar un bucle for para recorrer la cadena y un condicional if
# para comprobar si cada carácter es una vocal.

def contar_vocales(cadena):
    contador = 0
    lista_vocales = []
    
    for i in range(len(cadena)):
        if cadena[i] == "A" or cadena[i] == "E" or cadena[i] == "I" or cadena[i] == "O" or cadena[i] == "U" or cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
            contador += 1
            lista_vocales.append(cadena[i])
            
    vocales = ", ".join(lista_vocales)
    
    return contador, vocales

def main():
    cadena = input("Ingrese una cadena: ")
    contador, vocales = contar_vocales(cadena)
    print("Cantidad de vocales: ",contador)
    print("Las vocales: ", vocales)
    
main()
# 1.Desarrollar una función que determine si una cadena de caracteres es capicúa. Escribir además un programa que permita
# verificar su funcionamiento solicitándole al usuario valores hasta que el mismo sea vacío.

def capicua(msj):
    msj_invertido = msj[::-1]
    
    if msj == msj_invertido:
        print("La palabra es capicua")
    elif msj != msj_invertido:
        print("La palabra no es capicua")
    
    return msj_invertido
    

def main():
    msj = input("Ingrese una palabra: ")
    msj_invert = capicua(msj)
    print("Palabra: ",msj)
    print("Palabra invertida: ",msj_invert)
    
main()
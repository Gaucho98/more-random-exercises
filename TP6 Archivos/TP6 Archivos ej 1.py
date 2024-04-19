# 1. Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un fichero de texto llamado “frases.txt”.
# Terminará cuando la frase introducida sea "fin" (esa frase no deberá guardarse en el fichero).

try:
    archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/frases.txt","w")
    
    frase = input("Ingrese una frase: ")
    while frase != "fin":
        print(frase, file = archivo)
        frase = input("Ingrese una frase: ")
        
    archivo.close()
    
except:
    print("Archivo no encontrado.")

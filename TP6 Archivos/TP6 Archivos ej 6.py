# 6.Genere un programa que pregunte un nombre de archivo (ubicación) y muestre en pantalla el contenido de ese archivo.
# Informe en pantalla si no existe.

nombre_archivo = input("Ingrese el nombre del archivo que desea buscar: ")

try:
    archivo = open(nombre_archivo,"r")
    
    for linea in archivo:
        print(linea)
        
    archivo.close()
    
except:
    print("El archivo no existe.")
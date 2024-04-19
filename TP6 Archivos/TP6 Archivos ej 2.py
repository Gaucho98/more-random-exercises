# 2. En base al primer punto, luego de generar la carga de las frases, visualizar el archivo cargado.

try:
    archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/frases.txt","r")
    
#     for frase in archivo:
#         print(frase)

    linea = archivo.read()
    print(linea)
    
    archivo.close()
except:
    print("Archivo no encontrado.")
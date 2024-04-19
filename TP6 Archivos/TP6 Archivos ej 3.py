# 3.Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores numéricos. Realizar un proceso que visualice
# su contenido y, al finalizar, muestre el total (sumatoria de los valores) y promedio.

# try:
#     archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/montos.txt","w")
#     
#     monto = input("Ingrese el monto: ")
#     while monto != "fin":
#         print(monto, file = archivo)
#         monto = input("Ingrese el monto: ")
#            
#     archivo.close()
#     
# except:
#     print("Error.")
    
try:
    archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/montos.txt","r")
    
    linea = archivo.read()
    lista_montos = linea.split("\n")
    i = 1
    lista_int = []
    
    for monto in lista_montos:
        print(f"Monto {i}: ${monto}")
        i += 1
        int_monto = int(monto)
        lista_int.append(int_monto)
        
    suma = sum(lista_int)
    print(f"Total: ${suma}")
    
    promedio = suma / i
    print(f"Promedio: ${promedio}")
    
    archivo.close()
    
except:
    print("Error.")
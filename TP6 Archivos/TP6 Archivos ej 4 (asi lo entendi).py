# 4. Crear un programa que maneje un archivo donde se almacena la siguiente información de una determinada cantidad personas:
# Nombre, Apellido, Edad y Estatura. El programa deberá almacenar la información a medida que se vayan cargando. El formato
# a ser almacenado será cada dato separado por el carácter punto y coma (;) en el mismo orden que se carga. Tenga en cuenta
# que cada vez que se ejecuta el programa, se debe incrementar el contenido del archivo (agregar al final).

try:
    archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/Personas.txt","r")
            
    lineas = archivo.read()
    lista_lineas = lineas.split()
        
    lista = []
        
    for i in range(len(lista_lineas)):
        split_datos = lista_lineas[i].split(";")
        lista.append(split_datos)
            
    for i in range(len(lista)):
        print(f"Nombre: {lista[i][0]} | Apellido: {lista[i][1]} | Edad: {lista[i][2]} | Estatura: {lista[i][3]}")
         
    archivo.close()

except:
    print("Error.")
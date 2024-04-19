# 4. Crear un programa que maneje un archivo donde se almacena la siguiente información de una determinada cantidad personas:
# Nombre, Apellido, Edad y Estatura. El programa deberá almacenar la información a medida que se vayan cargando. El formato
# a ser almacenado será cada dato separado por el carácter punto y coma (;) en el mismo orden que se carga. Tenga en cuenta
# que cada vez que se ejecuta el programa, se debe incrementar el contenido del archivo (agregar al final).

try:
    archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/Personas2.txt","a")
    
    flag = True
    
    while flag != False:
        nom = input("Nombre: ")
        apell = input("Apellido: ")
        edad = input("Edad: ")
        est = input("Estatura: ")
        archivo.write(f"{nom};{apell};{edad};{est};\n")
        continuar = input("¿Desea continuar? S/N: ")
        if continuar == "n" or continuar == "N":
            flag = False
        elif continuar == "s" or continuar == "S":
            flag = True
    
    archivo.close()
    
except:
    print("Error.")
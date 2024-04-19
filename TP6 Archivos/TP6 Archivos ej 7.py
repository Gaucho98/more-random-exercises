# 7.Crear dos archivos:
# .: Paises.txt -> Con el contenido de los países de Latinoamérica
# .: Provincias.txt -> Con el contenido de las provincias de Argentina
# 
# Crear un programa que le pregunte al usuario si quiere ver los países o provincias, de acuerdo a su selección, debe mostrar su
# contenido en pantalla (que elija 1 o 2 con el teclado).
try:
    elecc = int(input("¿Desea ver provincias? (Presione 1) /// ¿Desea ver paises? (Presione 2): "))
except:
    print("El valor ingresado debe ser un numero entero.")
try:
    if elecc == 1:
        archivo_paises = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/paises.txt","r", encoding="UTF-8")
        lectura_archivo_paises = archivo_paises.read()
        print(lectura_archivo_paises)
        archivo_paises.close()
    elif elecc == 2:
        archivo_provincias = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/provincias.txt","r", encoding="UTF-8")
        lectura_archivo_provincias = archivo_provincias.read()
        print(lectura_archivo_provincias)
        archivo_provincias.close()
except:
    print("Error.")

    
# 5.Crear un programa que permita recuperar la información del archivo generado y muestre los promedios de edad y estaturas.
# Muestre todos los datos al procesar.

archivo = open("C:/Users/ALPHA/Desktop/Thonny guardados/Ejercicios UADE Python 2do cuatrimestre ALGORITMIA Y ESTRUCTURA DE DATOS I/TP6 Archivos/archivos/Personas.txt", "r")

datos = []

for linea in archivo:
    lin = linea.split(";")
    datos.append(lin)
    
edades = []
alturas = []

for j in range(len(datos)):
    edades.append(datos[j][2])
    alturas.append(datos[j][3])
    
edades_int = []
alturas_int = []

for i in range(len(datos)):
    int_edad = int(edades[i])
    edades_int.append(int_edad)
    int_alt = float(alturas[i])
    alturas_int.append(int_alt)

print(edades_int)
print(alturas_int)
    
suma_edad = sum(edades_int)
suma_alt = sum(alturas_int)

prom_edad = suma_edad / 4
prom_alt = suma_alt / 4

archivo.close()

print(f"El promedio de edad es: {prom_edad}")
print(f"El promedio de altura es: {prom_alt}")
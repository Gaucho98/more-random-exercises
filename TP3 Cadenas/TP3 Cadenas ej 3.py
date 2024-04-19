# 3. Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra",
# cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos
# ubicados en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en posiciones pares. Los dígitos
# se numeran desde la izquierda. Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.

clave_maestra = "18293"

clave1 = clave_maestra[0::2]
clave2 = clave_maestra[1::2]

print("Clave maestra: ",clave_maestra)
print("Clave 1: ",clave1)
print("Clave 2: ",clave2)
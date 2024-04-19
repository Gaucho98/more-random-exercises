# 2. Crear tres conjuntos:
# • pares: valores pares entre 0 y 100
# • impares: valores impares entre 0 y 100
# • azar: 50 valores al azar entre 0 y 100
# Una vez generados los tres conjuntos, deberá realizar las siguientes acciones:
# • generar dos nuevos conjuntos: uno con la intersección entre azar y pares; y azar e impares.
# Informe de cada uno de ellos: la cantidad, el valor máximo y mínimo.
import random

pares = {i for i in range(0,101) if i % 2 == 0}
print(f"Pares: {pares}\n")
impares = {i for i in range(0,101) if i % 2 != 0}
print(f"Impares: {impares}\n")
azar = {random.randint(0,100) for i in range(0,50)}
print(f"Numeros al azar: {azar}\n")
print(f"Interseccion entre azar y pares: {azar & pares}")
print(f"Cantidad de numeros: {len(azar & pares)} - Valor maximo: {max(azar & pares)} - Valor minimo: {min(azar & pares)}\n")
print(f"Interseccion entre azar e impares: {azar & impares}")
print(f"Cantidad de numeros: {len(azar & impares)} - Valor maximo: {max(azar & impares)} - Valor minimo: {min(azar & impares)}\n")







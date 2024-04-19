# 6. Modifique la función anterior, haciendo uso de filter, para poder obtener una lista de notas aprobadas y otro de
# desaprobadas.

import random

lista_notas = [random.randint(1,10) for i in range(10)]
print("Lista de notas: ",lista_notas)

lista_aprobados = list(filter(lambda lista : lista if lista >= 4 else None, lista_notas))
print("Notas aprobadas: ", lista_aprobados)

lista_desaprobados = list(filter(lambda lista : lista if lista < 4 else None, lista_notas))
print("Notas desaprobadas: ", lista_desaprobados)
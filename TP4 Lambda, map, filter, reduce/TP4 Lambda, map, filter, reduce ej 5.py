#5. Utilizando map, crear un programa que cargue 10 notas de alumnos y, al finalizar, genere una nueva lista indicando el
# estado de aprobación (reutilice lo creado en el punto 1).

import random

lista_notas = [random.randint(1,10) for i in range(10)]
print("Lista de notas: ",lista_notas)

lista_estado = list(map(lambda lista : "Desaprobado" if lista < 4 else "Aprobado", lista_notas))
print("Estado de aprobacion: ", lista_estado)
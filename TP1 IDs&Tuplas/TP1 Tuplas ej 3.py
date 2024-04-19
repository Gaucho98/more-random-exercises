# Desarrolle un programa que procese una tabla con 10 horarios (hora -de 0 a 23- y minutos) en formato tupla; e indique por
# cada una de ellas: si es AM o PM y cuántos minutos falta para la próxima hora. El resultado de AM/PM y la cantidad de minutos
# se debe almacenar en una lista de tuplas con los valores originales y los resultados. Imprimir el resultado final en pantalla.

import random

def tabla():
    lalista = []
    
    for i in range(10):
        hora = random.randint(0,23)
        minuto = random.randint(0,59)
        lista = []
        lista.append(hora)
        lista.append(minuto)
        listaATupla = tuple(lista)
        lalista.append(listaATupla)
        
    return lalista

def calculo_horario(lista1):
    min = 60
    lista2 = []
    
    for i,j in lista1:
        if i <= 12:
            lista = []
            min -= j
            lista.append("AM")
            lista.append(min)
            tupla = tuple(lista)
            lista2.append(tupla)
        elif i > 12:
            lista = []
            min -= j
            lista.append("PM")
            lista.append(min)
            tupla = tuple(lista)
            lista2.append(tupla)
        min = 60
        
    return lista2

def impresion(lista1,lista2):
    for i in range(len(lista1)):
        print(lista1[i],"-->",lista2[i])
    
def main():
    lista1 = tabla()
    lista2 = calculo_horario(lista1)
    impresion(lista1,lista2)
    
main()
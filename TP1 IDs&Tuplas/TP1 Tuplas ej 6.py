# Cálculo de promedio: crea un programa que lea una lista de tuplas, donde cada tupla contiene el nombre de un estudiante y
# una lista de calificaciones, y calcule el promedio de calificaciones de cada estudiante.
# Por ejemplo, si llamamos a la función con la lista de tuplas
# [( 'Juan', [9, 8, 7]), ('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])], la función devolverá la lista
# [( 'Juan', 8.0), ('Maria', 9.67), ('Pedro', 8.0)], que contiene el nombre de cada estudiante y su promedio de calificaciones
# en forma de tuplas.

def calculo_promedio(lista_tuplas):
    acu = 0
    lista_sumas = []
    lista_nombres = []
    lista_notas = []
    lista_promedio = []
    tupla_promedios = []
    
    for i in range(len(lista_tuplas)):
        tupla = lista_tuplas[i]
        for j in range(len(lista_tuplas[i])):
            suma = sum(tupla[1])
        lista_sumas.append(suma)
        lista_nombres.append(tupla[0])
        acu += 1
        
    for i in range(len(lista_sumas)):
        nota = lista_sumas[i] // acu
        lista_notas.append(nota)
    
    for i in range(len(lista_tuplas)):
        lista = []
        lista.append(lista_nombres[i])
        lista.append(lista_notas[i])
        lista_promedio.append(lista)
        
    for i in range(len(lista_promedio)):
        lista_a_tupla = tuple(lista_promedio[i])
        tupla_promedios.append(lista_a_tupla)
    
    return tupla_promedios
            
def main():
    lista_tuplas = [("Juan",[9,8,7]),("Maria",[10,9,10]),("Pedro",[8,7,9])]
    tupla_promedios = calculo_promedio(lista_tuplas)
    print(tupla_promedios)
    
main()
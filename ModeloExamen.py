# 1.
def lista_de_multiplios(desde,hasta,multiplo_de):
    lista = [i for i in range(desde,hasta) if i % multiplo_de == 0]
    print("a.", lista)
    
def solo_numeros(cadena):
    nueva_cadena = cadena[-3::]
    print("b.", nueva_cadena)
    
def ultimo_y_primer_caracter(cadena2):
    salto = len(cadena2)
    nueva_cadena2 = cadena2[0::salto-1]
    print("c.", nueva_cadena2)
    
def promedio_calificaciones(lista):
    lista2 = []
    for i in range(len(lista)):
        tuplaAlista = list(lista[i])
        lista2.append(tuplaAlista)
    
    lista3 = []
      
    for i in range(len(lista2)):
        lista3.append(lista2[i][1])
    
    lista3b = []
    
    for i in range(len(lista2)):
        lista3b.append(lista2[i][0])
    
    lista4 = []
    
    for i in range(len(lista3)):
        suma = sum(lista3[i])
        lista4.append(suma)
    
    lista5 = []
    
    for i in range(len(lista4)):
        promedio = lista4[i] / 3
        lista5.append(promedio)
        
    lista6 = []
    
    for i in range(len(lista5)):
        lista = []
        lista.append(lista3b[i])
        lista.append(lista5[i])
        lista6.append(lista)
        
    lista7 = []
    
    for i in range(len(lista6)):
        listaAtupla = tuple(lista6[i])
        lista7.append(listaAtupla)
    print("d.", lista7)

def suma_lista_tuplas(listaDetuplas):
    lista = []
    
    for i in range(len(listaDetuplas)):
        tuplaAlista = list(listaDetuplas[i])
        lista.append(tuplaAlista)
    
    lista2 = []
    
    for i in range(len(lista)):
        suma = sum(lista[i])
        lista2.append(suma)
    print("e.", lista2)

def alternar_contenidos(tupla1,tupla2):
    lista = []
    
    tuplaAlista1 = list(tupla1)
    tuplaAlista2 = list(tupla2)
    
    for i in range(len(tuplaAlista1)):
        lista.append(tuplaAlista1[i])
        lista.append(tuplaAlista2[i])
        
    listaAtupla = tuple(lista)
    print("f.", listaAtupla)
    
def resultado_aprobadcion(notas):
    condiciones = list(map(lambda numero : "Aprobado" if numero >= 4 else "Desaprobado", notas))
    print("g.", condiciones)
    
def separar_notas(notas):
    aprobados = list(filter(lambda numero : numero if numero >= 4 else None, notas))
    desaprobados = list(filter(lambda numero : numero if numero < 4 else None, notas))
    print("h.", desaprobados, aprobados)
    
def nota_mas_alta(notas):
    from functools import reduce
    return reduce(lambda a,b : a if a > b else b, notas)
        
def main():
    desde = 1
    hasta = 10
    multiplo_de = 3
    lista_de_multiplios(desde,hasta,multiplo_de)
    cadena = "Oliver123"
    solo_numeros(cadena)
    cadena2 = "Oliver"
    ultimo_y_primer_caracter(cadena2)
    lista = [("Juan",[9,8,7]),("Maria",[10,9,10]),("Pedro",[8,7,9])]
    promedio_calificaciones(lista)
    listaDetuplas = [(1,2),(3,4),(5,6,7)]
    suma_lista_tuplas(listaDetuplas)
    tupla1 = (1,2,3)
    tupla2 = (4,5,6)
    alternar_contenidos(tupla1,tupla2)
    notas = [2,4,6]
    resultado_aprobadcion(notas)
    separar_notas(notas)
    nota = nota_mas_alta(notas)
    print("i.", nota)
    
main()

print("------------------------------------------------------------------------------------------------------")

#2.
def funcion_a():
    cadena = "Hoy es Domingo"
    lista = [cadena[i] for i in range(len(cadena)) if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u" or cadena[i] == "A" or cadena[i] == "E" or cadena[i] == "I" or cadena[i] == "O" or cadena[i] == "U"]
    print("a.", lista)
    
def funcion_b():
    lista = [i for i in range(1,100) if i % 7 == 0 or i % 8 == 0]
    print("b.", lista)
    
def funcion_c():
    lista = [i for i in range(120) if i % 3 == 0 and i % 2 == 1]
    print("c.", lista)
    
def funcion_d():
    variable_nombres = ["marcos","alan","pablo","irma"]
    lista = [nombre.title() for nombre in variable_nombres if nombre[0] == "a" or nombre[0] == "e" or nombre[0] == "i" or nombre[0] == "o" or nombre[0] == "o"]
    print("d.", lista)

def funcion_e():
    lista = [i for i in range(0,100) if i % 4 == 0 and i % 6 != 0]
    print("e.", lista)

def main():
    funcion_a()
    funcion_b()
    funcion_c()
    funcion_d()
    funcion_e()
    
main()
# 7.Cálculo de áreas: crea un programa que lea una lista de tuplas, donde cada tupla contiene el nombre de una figura
# geométrica (cuadrado, rectángulo, triángulo y círculo)  y sus dimensiones, y calcule el área de cada figura.

def calculo_area(lista):
    lista2 = []
    for i in range(len(lista)):
        tuplaAlista = list(lista[i])
        lista2.append(tuplaAlista)
    
    lista3 = []
    for i in range(len(lista2)):
        for j in range(len(lista2[i])):
            suma = sum(lista2[i][1])
        lista3.append(suma)
    
    lista4 = []
    for i in range(len(lista2)):
        lista = []
        lista.append(lista2[i][0])
        lista.append(lista3[i])
        lista4.append(lista)
    
    lista5 = []
    for i in range(len(lista4)):
        listaAtupla = tuple(lista4[i])
        lista5.append(listaAtupla)
    return lista5
            
def main():
    lista = [("Cuadrado",[10,10,10,10]),("Rectangulo",[20,10,20,10]),("Triangulo",[10,10,10]),("Circulo",[30])]
    nueva_lista = calculo_area(lista)
    print("Lista de figuras con sus dimensiones:\n",lista)
    print("Lista de figuras con el calculo de su area:\n", nueva_lista)
    
main()
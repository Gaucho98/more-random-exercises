def carga_notas():
    lista_notas = [1,9,5,2,6,3,7,4,8,10]
    lista_condicion = []
    
    for i in range(len(lista_notas)):
        if lista_notas[i] == 0:
            lista_condicion.append("Ausente")
        elif lista_notas[i] >= 1 and lista_notas[i] <= 3:
            lista_condicion.append("Desaprobado")
        elif lista_notas[i] >= 4 and lista_notas[i] <= 6:
            lista_condicion.append("Aprobado")
        elif lista_notas[i] >= 7 and lista_notas[i] <= 10:
            lista_condicion.append("Promocionado")
            
    return lista_notas,lista_condicion
    
def main():
    lista_notas,lista_condicion = carga_notas()
    print("Lista de notas: ",lista_notas)
    print("Lista condicion final: ",lista_condicion)
    
main()
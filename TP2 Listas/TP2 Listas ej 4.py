# 4. Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la lista original,
# la lista de palabras a eliminar y la lista resultante.

def funcion_eliminar(lista1,lista2):
    lista3 = []
    
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista3.append(lista1[i])
            
    lista4 = [lista1[i] for i in range(len(lista1)) if lista1[i] not in lista2]
    
    return lista3,lista4

def main():
    lista1 = ["Pato","Leon","Elefante","Tortuga","Jirafa","Tigre","Alcon"]
    lista2 = ["Elefante","Tortuga","Jirafa"]
    lista3,lista4 = funcion_eliminar(lista1,lista2)
    print("Lista original: ",lista1)
    print("Lista de palabras a eliminar: ",lista2)
    print("Lista resultante: ",lista3)
    print("Lista resultante (hecho con comprension de listas): ",lista4)
    
main()
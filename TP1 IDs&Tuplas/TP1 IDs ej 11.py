# Crear una función que reciba dos listas como parámetros. Dentro de la función, concatenar ambas listas y comprobar si el ID
# de la lista concatenada ha cambiado o se ha mantenido igual.

def concatenacion(listaA,listaB):
    listaC = []
    
    print(id(listaC)) #(?
    
    for i in range(len(listaA)):
        listaC.append(listaA[i])
        listaC.append(listaB[i])
        
    print(id(listaC))
    
    return listaC
        
listaA = [1,3,5]
listaB = [2,4,6]
print(id(listaA))
print(id(listaB))
listaC = concatenacion(listaA,listaB)
print(id(listaC))
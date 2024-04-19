#  Crear una función que reciba una lista como parámetro. Dentro de la función, crear una nueva lista y asignarla a la variable
#  original. Imprimir los IDs de ambas listas antes y después de la asignación dentro de la función. ¿Qué puedes concluir sobre
#  el comportamiento de Python en este caso?

def funcion_lista(listaA):
    listaB = listaA
    return listaB
    
def main():
    listaA = [1,2,3,4]
    print("Antes: ", id(listaA))
    listaB = funcion_lista(listaA)
    print("Despues: ", id(listaB))

main()

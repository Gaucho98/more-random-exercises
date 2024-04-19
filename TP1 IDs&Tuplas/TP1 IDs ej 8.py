# Crear una lista y asignarla a otra variable diferentes. Luego, imprimir los IDs de ambas 
# variables y comprobar si son iguales o diferentes. ¿Qué puedes concluir sobre el comportamiento de Python en este caso?

listaA = [1,2,3,4,5]
listaB = listaA

a = id(listaA)
b = id(listaB)

print("El ID de listaA: ", a)
print("El ID de listaB: ", b)

print("listaA es igual a listaB: ", a == b)
print("listaA es listaB: ", a is b)

# Lo que puedo concluir en este comportamiento es que el objeto que se guarda en la variable de listaA y listaB son iguales, por
# eso cuando imprimo "a == b" da como resultado "True".
# Pero cuando comparo listaA con listaB da como resultado "False" porque son variables que estan guardadas en distinta posicion.
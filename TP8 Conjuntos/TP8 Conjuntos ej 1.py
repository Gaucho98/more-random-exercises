# 1. Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto
# mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al
# ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

conjunto = {0,1,2,3,4,5,6,7,8,9}
print(f"Conjunto --> {conjunto}")
valor = int(input("Ingrese un valor a eliminar del conjunto: "))
while valor != -1:
    try:
        conjunto.remove(valor)
        print(f"Conjunto --> {conjunto}")
    except:
        print("El valor no se encuentra en el conjunto.")
    valor = int(input("Ingrese otro valor a eliminar del conjunto: "))
print("Fin del programa.")
















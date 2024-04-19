# 4. El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa. Sin embargo,
# si el elemento no pertenece a la lista se produce una excepción de tipo ValueError. Desarrollar un programa que cargue una
# lista con números enteros ingresados a través del teclado (terminando con -1) y permita que el usuario ingrese el valor de
# algunos elementos para visualizar la posición que ocupan, utilizando el método index. Si el número no pertenece a la lista
# se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el proceso al tercer error detectado.
# No utilizar el operador in durante la búsqueda.

def generacion_de_lista():
    lista = []
    
    num = int(input("Ingrese un numero: "))
    while num != -1:
        lista.append(num)
        msj = input("¿Desea visualizar la posicion de un numero? si o no: ")
        if msj == "si":
            try:
                num_index = int(input("Ingrese un numero para saber su posicion: "))
                print("El numero ingresado se encuentra en la posicion: ", lista.index(num_index))
            except:
                i = 0
                
                while num_index not in lista:
                    print("El numero no se encuentra en la lista, intente nuevamente.")
                    num_index = int(input("Ingrese un numero para saber su posicion: "))
                    i += 1
                    if num_index in lista:
                        print("El numero ingresado se encuentra en la posicion: ", lista.index(num_index))
                    if i == 2:
                        return "Fin del programa"
        num = int(input("Ingrese un numero: "))
    
    return lista

def main():
    mensaje = generacion_de_lista()
    print(mensaje)
    
main()
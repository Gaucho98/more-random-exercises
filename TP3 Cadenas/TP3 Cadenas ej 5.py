# 5.Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la cantidad
# de caracteres deseada. Devolver la subcadena como valor de retorno. Escribir también un programa para verificar el
# comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que
# comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función utilizando
# rebanadas.

def extraccion_subcadena(cadena):
    i = int(input("Ingrese la posicion a partir de la cual se extraera la subcadena: "))
    j = int(input("Cuantos caracteres desea extraer? "))
    
    nueva_cadena = cadena[i:i+j:]
    return nueva_cadena

def main():
    cadena = "El número de teléfono es 4356-7890"
    nueva_cadena = extraccion_subcadena(cadena)
    print(nueva_cadena)
    
main()
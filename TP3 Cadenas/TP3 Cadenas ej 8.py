# 8.Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y
# devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben
# reemplazarse palabras completas, y no fragmentos de palabras. Escribir también un programa para verificar el
# comportamiento de la función.

def reemplazar_apariciones():
    cadena = "Perro tierno, perro lindo, perro dulce, perro peludo"
    cadena2 = (cadena.replace("Perro","Gato"))
    cadena3 = (cadena2.replace("perro","gato"))
    
    contador = 0
    lista_cadena = cadena.split()
    
    for i in lista_cadena:
        if i == "Perro" or i == "perro":
            contador += 1
            
    return cadena,cadena3,contador
    
def main():
    cadena,cadena3,contador = reemplazar_apariciones()
    print("Cadena original: ", cadena)
    print("Cadena modificada: ", cadena3)
    print("Cantidad de cambios: ",contador)
    
main()
# 7. Cuenta la cantidad de palabras únicas en una cadena: Crea una función que tome una cadena como argumento y devuelva
# la cantidad de palabras únicas en la cadena. Para hacerlo, puedes utilizar conjuntos y el método len() de Python.

def palabras_unicas(cadena):
    lista_cadena = cadena.split()
    conjunto = set([])
    for i in range(len(lista_cadena)):
        conjunto.add(lista_cadena[i])
    return len(conjunto)
    
def main():
    cadena = "Hoy es martes y esta soleado y es un buen dia dia dia "
    cantidad_palabras = palabras_unicas(cadena)
    print("La cantidad de palabras unicas es: ", cantidad_palabras)
    
main()
# 6.Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas
# por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una.

def ordenar_palabras(cadena):
    lista = cadena.split()
    lista.sort()
    cadena2 = " ".join(lista)
    print(cadena2)
    
def main():
    cadena = "la   calesita gira      rapido"
    ordenar_palabras(cadena)
    
main()
# 6. Palabras únicas en una cadena: Crea una función que tome una cadena como argumento y devuelva un conjunto que contenga
# todas las palabras únicas en la cadena.

def cadena_en_conjunto(cadena):
    lista_cadena = cadena.split()
    conjunto = set([])
    
    for i in range(len(lista_cadena)):
        conjunto.add(lista_cadena[i])
    return conjunto
    
def main():
    cadena = "Hoy es martes y esta soleado"
    cadena_conjunto = cadena_en_conjunto(cadena)
    print(cadena_conjunto)
    
main()
# // Otra manera de hacerlo //
# def cadena_en_conjunto(cadena):
#     lista_cadena = cadena.split()
#     return {lista_cadena[i] for i in range(len(lista_cadena))}
#     
# def main():
#     cadena = "Hoy es martes y esta soleado"
#     print(cadena_en_conjunto(cadena))
#     
# main()
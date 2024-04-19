# 5. Eliminar duplicados de una lista con conjuntos: Crea una función que tome una lista y elimine los elementos duplicados
# utilizando conjuntos. La función debe devolver una lista sin elementos duplicados.

def eliminar_duplicados(lista):
    return list(set(lista))

def main():
    lista = [1,1,2,3,3,3,4,4,5,6,7,7,2]
    print(lista)
    print(eliminar_duplicados(lista))
    
main()
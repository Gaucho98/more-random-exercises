# 8. Contar elementos únicos en una lista: Crea una función que tome una lista como argumento y devuelva el número de
# elementos únicos en la lista.

def elementos_unicos(lista):
    conjunto = set([])
    for i in range(len(lista)):
        conjunto.add(lista[i])
    return len(conjunto)
    
def main():
    lista = [1,1,2,2,3,3,4,4,5,5]
    cantidad = elementos_unicos(lista)
    print(f"La cantidad de elementos unicos es: {cantidad}")
    
main()
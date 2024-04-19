# 9. Crear una lista de valores únicos a partir de un diccionario: Crea una función que tome un diccionario como argumento
# y devuelva una lista con los valores únicos del diccionario.

def valores_unicos(numeros):
    conjunto = set([])
    lista_numeros = list(numeros.values())
    for i in range(len(lista_numeros)):
        conjunto.add(lista_numeros[i])
    return list(conjunto)
    
def main():
    numeros = {
        'uno' : 1,
        'dos' : 2,
        'tres' : 3,
        'cuatro' : 3,
        'cinco' : 3,
        }
    unicos = valores_unicos(numeros)
    print(f"Lista con valores unicos del diccionario: {unicos}")
    
main()
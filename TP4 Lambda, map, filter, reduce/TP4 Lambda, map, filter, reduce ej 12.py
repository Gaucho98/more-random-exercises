# 12.Crea una función ordenaPalabras que acepte una lista de palabras como argumento, y devuelva una nueva lista con las
# palabras ordenadas alfabéticamente en orden inverso. Utiliza funciones lambda, map y sorted para implementarla.

lista = ["Barco", "Casa", "Arbol", "Empanada", "Dentista"]

def ordenaPalabras(lista):
    lista2 = []
    lista2.append(lista)
    ordenado = list(map(lambda palabra : sorted(palabra)[::-1], lista2))
    for i in range(len(ordenado)):
        return ordenado[i]

print("Lista: ",lista)
print("Lista con las palabras ordenadas alfabéticamente en orden inverso: ", ordenaPalabras(lista))
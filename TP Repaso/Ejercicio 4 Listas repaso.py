def combinar_listas(lista1,lista2):
    lista3 = []
    
    if len(lista1) > len(lista2):
        for i in range(len(lista2)):
            lista3.append(lista1[i])
            lista3.append(lista2[i])
    elif len(lista1) < len(lista2):
        for i in range(len(lista1)):
            lista3.append(lista1[i])
            lista3.append(lista2[i])
    
    return lista3

def impresion(listas_combinadas):
    print("Listas combinadas: ",listas_combinadas)

def main():
    lista1 = ["Hola","nombre","Juan"]
    lista2 = ["mi","es","Perez"]
    listas_combinadas = combinar_listas(lista1,lista2)
    impresion(listas_combinadas)
    
main()
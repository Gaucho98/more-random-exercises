def combinar_listas(lista1,lista2):
    lista3 = []
    
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        
    if len(lista1) != len(lista2):
        return("El proceso no se puede realizar.")
        
    return lista3

def impresion(listas_combinadas):
    print("Listas combinadas: ",listas_combinadas)

def main():
    lista1 = ["Hola","nombre","Juan"]
    lista2 = ["mi","es","Perez"]
    listas_combinadas = combinar_listas(lista1,lista2)
    impresion(listas_combinadas)
    
main()
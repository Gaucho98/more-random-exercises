def intercambio(lista):
    primer_numero = lista[0]
    ultimo_numero = lista[len(lista)-1]
    
    del(lista[0])
    del(lista[len(lista)-1])
    
    lista.append(primer_numero)
    lista.insert(0,ultimo_numero)
    
    return lista

def impresion(lista_nueva):
    print("Lista con primer y ultimo valor intercambiados: ", lista_nueva)
    
def main():
    lista = [1,2,6,3,4,5,6,6,4,2,0]
    lista_nueva = intercambio(lista)
    impresion(lista_nueva)
    
main()
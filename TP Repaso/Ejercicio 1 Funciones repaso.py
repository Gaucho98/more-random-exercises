def pares_desde_hasta(desde,hasta):
    lista = []
    
    for i in range(desde,hasta):
        if i % 2 == 0:
            lista.append(i)
            
    return lista
    
def main():
    desde = int(input("Desde: "))
    hasta = int(input("Hasta: "))
    lista = pares_desde_hasta(desde,hasta)
    print(lista)
    
main()
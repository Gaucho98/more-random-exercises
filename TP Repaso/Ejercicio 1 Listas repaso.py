def encontrar_ocurrencias(lista,numero_ingresado):
    contador = 0
    
    for i in range(len(lista)):
        if lista[i] == numero_ingresado:
            contador += 1
    
    return contador
    
def impresion(ocurrencias):
    print("Cantidad de ocurrencias: ", ocurrencias)

def main():
    lista = [1,2,6,3,4,5,6,6,4,2,0]
    numero_ingresado = int(input("Ingrese un numero: "))
    ocurrencias = encontrar_ocurrencias(lista,numero_ingresado)
    impresion(ocurrencias)

main()
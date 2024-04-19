def eliminacion_elementos(lista,valor):
    lista2 = []
    
    for i in range(len(lista)):
        if valor != lista[i]:
            lista2.append(lista[i])
            
    return lista2

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    valor = int(input("Ingrese un valor: "))
    lista_sin_valor = eliminacion_elementos(lista,valor)
    print(lista_sin_valor)
    
main()
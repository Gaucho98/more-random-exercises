# 8. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5.
# A y B se ingresan desde el teclado.

def lista_multiplo():
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))
#     lista = []
#     
#     for i in range(a,b):
#         if i % 7 == 0 and not i % 5 == 0:
#             lista.append(i)
            
    lista = [i for i in range(a,b) if i % 7 == 0 and not i % 5 == 0]
            
    return lista
    
def main():
    lista = lista_multiplo()
    print(lista)
    
main()
# 7.Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos
# entre 100 y 200.

def lista_impares():
#     lista = []
#     
#     for i in range(100,200):
#         if i % 2 == 0:
#             lista.append(i)
            
    lista = [i for i in range(100,200) if i % 2 == 0]
        
    return lista

def main():
    lista = lista_impares()
    print(lista)
    
main()
# 4. Crea una función para unir conjuntos: Crea una función que tome dos conjuntos como argumentos y devuelva un conjunto
# que contenga todos los elementos de ambos conjuntos. Asegúrate de que la función maneje conjuntos con diferentes tipos de
# elementos, como cadenas y números.

def union_sets(set1,set2):
    return (set1 | set2)
    
def main():
    set1 = {1, 'uno' , 2, 'dos', 3, 'tres'}
    set2 = {4, 'cuatro', 5, 'cinco', 6, 'seis'}
    union = union_sets(set1,set2)
    print(union)
    
main()
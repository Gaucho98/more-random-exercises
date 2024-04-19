# 2. Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.

def producto(n1,n2):
    if n1 == 0 or n2 == 0:
        return 0
    elif n1 == 1 and n2 == 1:
        return 1
    elif n1 > n2:
        return n1 + producto(n1,n2-1)
    else:
        return n2 + producto(n1-1,n2)
    
def main():
    print(producto(0,0))
    print(producto(1,0))
    print(producto(0,1))
    print(producto(1,1))
    print(producto(2,1))
    print(producto(1,2))
    print(producto(3,25))
    
main()
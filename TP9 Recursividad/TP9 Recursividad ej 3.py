# 3. Escribir una función que devuelva la suma de los N primeros números naturales.
# n = 5 (5+4+3+2+1)

def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return n + sum(n-1)
    
def main():
    print(sum(10))
    
main()
# Escribir un programa que dadas dos tuplas de tres elementos, realice el producto de cada elemento existente en la primera
# tupla con todos los restantes del segundo y almacene cada resultado en otra tupla.
# Por ejemplo, el producto escalar entre (1, 2, 3) y (4, 5, 6); debería retornar: ((4, 5, 6),(8, 10, 12), (12, 15, 18)).

t1 = (1,2,3)
t2 = (4,5,6)

l3 = []

mult1 = 0

for i in range(len(t1)):
    mult1 = t1[0]*t2[i]
    l3.append(mult1)
    
l4 = []
    
mult2 = 0

for i in range(len(t1)):
    mult2 = t1[1]*t2[i]
    l4.append(mult2)
    
l5 = []
    
mult3 = 0

for i in range(len(t1)):
    mult3 = t1[2]*t2[i]
    l5.append(mult3)
    
LaT1 = tuple(l3)
LaT2 = tuple(l4)
LaT3 = tuple(l5)

print(LaT1,LaT2,LaT3)
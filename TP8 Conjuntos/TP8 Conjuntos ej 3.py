# 3. Crear dos conjuntos con cinco valores generados al azar, que se encuentre entre 1 y 10. Al finalizar, realizar:
# • Mostrar los valores que son en común entre ambos conjuntos.
# • Luego, volcar desde el primer conjunto al segundo, aquellos valores que no se encuentran del primero en el segundo.
import random

set1 = {random.randint(1,10) for i in range(5)}
set2 = {random.randint(1,10) for i in range(5)}
print(set1)
print(set2)
print(set1 & set2)
print(set1 - set2)
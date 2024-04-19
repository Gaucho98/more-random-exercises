#4. Escriba un programa Python para encontrar números divisibles por 3 de una lista de números usando Lambda.

lista = [1,2,3,8,9,15,27,29,30,299,300,3000,5894,9000]

nueva_lista = list(filter(lambda num : num % 3 == 0, lista))

print(nueva_lista)
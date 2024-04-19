diccionario = {'clave':'valor'}

conjunto = {'set1','set2','set2','set3'}
conjunto2 = set(['set1','set2','set2','set3'])
print(conjunto2)
print(conjunto)

numeros = {}
print(type(numeros))

pares = {i for i in range(0,101) if i % 2 == 0}
impares = [i for i in range(0,101) if i % 2 != 0]
pares.update(impares)
print(pares)
for i in range(len(pares)):
    if i % 2 == 0:
        pares.discard(i)
    elif i % 2 != 0:
        pares.remove(i)
print(pares)

d = [1,1,2,2,3,3,4,4,5,5]
sd = list(set(d))
print(sd)
print("--------------")
fibonacci = {0,1,1,2,3,5,8,13}
pares = {2,4,6,8,10}
print(f"fibonacci: {fibonacci}")
print(f"pares: {pares}")
print(fibonacci | pares)
print(fibonacci & pares)
print(fibonacci - pares)






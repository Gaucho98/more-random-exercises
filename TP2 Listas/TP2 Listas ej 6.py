# 6.Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse exclusivamente
# mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará la primera.
# Por ejemplo, si lista1 = [8, 1, 3] y lista2 =[5,9,7], lista1 deberá quedar como [8,5,1,9,3,7].

def funcion():
    lista1 = [8, 1, 3]
    lista2 =[5,9,7]
    
    lista1[1:1] = [lista2[0]]
    lista1[3:3] = [lista2[1]]
    lista1[5:5] = [lista2[2]]
    
    return lista1
    
def main():
    lista1 = funcion()
    print(lista1)
    
main()
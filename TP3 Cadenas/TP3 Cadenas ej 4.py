# 4. Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y
# devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa
# para verificar el comportamiento de la misma.

def filtrar_palabras(cadena,n):
    lista = cadena.split()
    lista2 = []

    for palabra in lista:
        if len(palabra) >= n:
            lista2.append(palabra)
            
    palabras_filtradas = " ".join(lista2)
    print(palabras_filtradas)
        
def main():
    cadena = input("Ingrese un mensaje: ")
    n = int(input("Ingrese N: "))
    filtrar_palabras(cadena,n)
    
main()
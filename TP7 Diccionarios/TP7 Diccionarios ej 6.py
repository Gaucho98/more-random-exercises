# 6. Juego de adivinanza de frutas: Crea un diccionario con nombres de frutas como claves y sus descripciones como valores.
# El programa debe elegir aleatoriamente una fruta y mostrar su descripción. Luego, el usuario debe adivinar qué fruta es.
# Si el usuario adivina correctamente, el programa debe mostrar un mensaje de felicitación.
import random

def adivinanza_frutas():
    frutas = {
        'Manzana':'Es roja y redonda',
        'Banana':'Es amarilla y larga',
        'Naranja':'Es redonda, naranja y tiene mucho jugo',
        'Pera':'Es verde, es ancha en su parte inferior y mas angosta en su parte superior',
        'Frutilla':'Es roja y tiene ojas verdes en su parte superior'
        }
    clave_aleatoria = random.choice(list(frutas.keys()))
    print("Adivine, ¿que fruta es? --> ", frutas[clave_aleatoria])
    
    fruta_ingresada = input("Ingrese la fruta: ")
    while fruta_ingresada != clave_aleatoria:
        fruta_ingresada = input("Intente nuevamente: ")
    if fruta_ingresada == clave_aleatoria:
        print("Felicidades, encontraste la fruta!")
            
def main():
    adivinanza_frutas()
    
main()
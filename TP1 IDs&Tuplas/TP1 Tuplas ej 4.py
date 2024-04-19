# Juego de cartas: crea una función que genere aleatoriamente una mano de cinco cartas de una baraja de póker. Cada carta debe
# ser representada por una tupla que contenga un número y un palo

import random

def mazo():
    mazo = []
    palo = ["trebol","corazones","picas","diamantes"]
    valor = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    
    for i in range(len(palo)):
        for j in range(len(valor)):
            carta = (valor[j],palo[i])
            mazo.append(carta)
    return mazo

def mano(elmazo):
    print("Mano: ")
    for i in range(5):
        num = random.randint(0,51)
        print(elmazo[num])
        
def main():
    elmazo = mazo()
    mano(elmazo)
    
main()
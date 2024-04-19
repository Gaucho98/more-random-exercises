# 10.Se desea implementar la funcionalidad del juego «piedra, papel o tijera». Para ello, se tiene una variable del tipo
# diccionario, en la que se almacena la regla de negocio de quién le gana a quién (la clave es el elemento, el valor a qué
# elemento le gana):
# 
# opcionesGanadoras = {
#     "piedra" : "tijera", 
#     "papel" : "piedra", 
#     "tijera" : "papel"
# }
# 
# En una segunda variable, se almacenan un lote (lista) de jugadas que deben ser procesadas, distinguiendo a dos jugadores,
# en los que se especifica como valor su nombre y la opción seleccionada en esa jugada:
# jugadas = [{
#     "jugador1" : {"nombre": "Oliver", "opcion": "piedra"},
#     "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
#     },
#     {
#     "jugador1" : {"nombre": "Oliver", "opcion": "tijera"},
#     "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
#     }]
# 
# Con relación a dicha información, se deberán elaborar las siguientes funciones: 
#  
# •resultado(opcion1, opcion2, opcionesGanadoras): Recibe como parámetro dos opciones (“piedra”, “papel” o “tijera”) junto
# con la variable de opcionesGanadoras. Deberá retornar None si hay un empate; 1 si gana la opción 1; y el valor 2 si gana la
# opción 2. Por ejemplo, dado los siguientes llamados, la función deberá retornar:
# resultado ('papel', 'papel', opcionesGanadoras) ==>  None
# resultado ('tijera', 'papel', opcionesGanadoras) ==>  1
# resultado ('tijera', 'piedra', opcionesGanadoras) ==>  2
# 
# •analizarJugada(jugada, opcionesGanadoras): Recibe una jugada como parámetros junto con las opciones ganadoras.
# Dentro de la función deberá utilizar la función resultado (definida en el ítem anterior) y retornar la leyenda:
# “Empate”, en caso de igualdad; o bien, “Gana {nombre del jugador}”. Utilizando las variables anteriores como ejemplo,
# debería retornar:
# analizarJugada({'jugador1': {'nombre': 'Oliver', 'opcion': 'piedra'}, 'jugador2': {'nombre': 'Gabriela', 'opcion': 'papel'}}, opcionesGanadoras) ==>  Gana Gabriela
# 
# analizarJugada({'jugador1': {'nombre': 'Oliver', 'opcion': 'tijera'}, 'jugador2': {'nombre': 'Gabriela', 'opcion': 'papel'}}, opcionesGanadoras) ==>  Gana Oliver

def resultado(opcion1, opcion2, opciones_ganadoras):
    for ganador, perdedor in opciones_ganadoras.items():
        if ganador == opcion1 and perdedor == opcion2:
            return 1
        elif ganador == opcion2 and perdedor == opcion1:
            return 2
        elif opcion1 == opcion2:
            return None
        
def analizar_jugada(jugadas, opciones_ganadoras):
    lista = []
    lista_nombre = []
    for jugador, datos in jugadas.items():
        lista.append(datos["opcion"])
        lista_nombre.append(datos["nombre"])
    
    for ganador, perdedor in opciones_ganadoras.items():
        if ganador == lista[0] and perdedor == lista[1]:
            return (f"Gana {lista_nombre[0]}")
        elif ganador == lista[1] and perdedor == lista[0]:
            return (f"Gana {lista_nombre[1]}")
        elif lista[0] == lista[1]:
            return "Empate"

def main():
    opcion1 = "piedra"
    opcion2 = "piedra"
    opciones_ganadoras = {
        "piedra" : "tijera", 
        "papel" : "piedra", 
        "tijera" : "papel"
    }
    jugadas = [
        {
            "jugador1" : {"nombre": "Oliver", "opcion": "piedra"},
            "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
            },
        {
            "jugador1" : {"nombre": "Oliver", "opcion": "tijera"},
            "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
            },
        {
            "jugador1" : {"nombre": "Oliver", "opcion": "papel"},
            "jugador2" : {"nombre": "Gabriela", "opcion": "papel"}
            }
        ]
    res = resultado(opcion1, opcion2, opciones_ganadoras)
    print(res)
    res2 = analizar_jugada(jugadas[1], opciones_ganadoras) # cambiar valor de jugadas[...] para cambiar la jugada
    print(res2)
    
main()
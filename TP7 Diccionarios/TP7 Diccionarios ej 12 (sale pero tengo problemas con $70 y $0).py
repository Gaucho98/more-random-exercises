# 12. Una imprenta debe realizar el cálculo total de la generación de letras corpóreas que le encargan sus clientes.
# Para ello, se tiene una variable con una cadena de caracteres corpóreas:
# 
# cadena = "Hola!"
# 
# Dicho costo dependerá del valor de cada uno de los caracteres que será almacenado en una segunda variable (diccionario),
# con el precio unitario de acuerdo con cada letra (agrupadas por lote):
# 
# precios = {
#     "qwertyuiopasdfghjklzxcvbnm0123456789":100,
#     "áéíóú":110,
#     "QWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚ": 180
# }
# 
# Contando con dicha información, deberá elaborar las siguientes funciones:
#     
# • precioPorLetra(letra, precios): que reciba la información de la letra y los precios y retorne el monto de esta de
# encontrarse en la clave. Si no se encuentra, el valor por defecto es de $70. Además, el espacio (“ “) tiene un valor de $0.
# Por ejemplo, si se recibe la letra “o”, el valor a retornar es de 100 y con “H” se retorna 180.
# • precioTotal(cadena, precios): que reciba la información de la cadena y retorna el monto total de la compra utilizando
# la función anterior (debe necesariamente incluirla para el cálculo). Por ejemplo, la cadena “Hola!” debería computarse su
# sumatoria de la siguiente manera:
# Letra: H --> $ 180
# Letra: o --> $ 100
# Letra: l --> $ 100
# Letra: a --> $ 100
# Letra: ! --> $ 70
# 
# Y el total que retornaría la función sería de $550

def precioPorLetra(letra, precios):
    for letras, precio in precios.items():
        if letra in letras:
            return precio
        elif letra == " ":
            return 0

def precioTotal(cadena, precios):
    cadena_l = []
    
    for i in range(len(cadena)):
        cadena_l.append(cadena[i])
    
    for i in cadena_l:
        for letras, precio in precios.items():
            if i in letras:
                print(f"Letra: {i} --> $ {precio}")
            elif i == " ":
                print(f"Letra: {i} --> $ {0}")
        
def main():
    letra = "Q"
    cadena = "Hola mundo"
    precios = {
        "qwertyuiopasdfghjklzxcvbnm0123456789":100,
        "áéíóú":110,
        "QWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚ": 180
        }
    precio_letra = precioPorLetra(letra, precios)
    print(f"El precio de {letra} es ${precio_letra}.")
    precioTotal(cadena, precios)
    
main()
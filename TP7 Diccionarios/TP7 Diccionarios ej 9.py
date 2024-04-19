# 9. Supongamos que un coleccionista de figuras Funko Pop de Rick y Morty tiene un carrito de compras con las siguientes figuras y
# sus respectivas cantidades:
# 
# carrito = { 
#     "Rick Sanchez" : 2, 
#     "Morty Smith" : 3, 
#     "Summer Smith" : 1,
#     "Mr. Meeseeks" : 4
# }
# 
# Y además, el coleccionista conoce los precios unitarios (en dólares) de estas figuras:
# 
# precios = {
#     "Rick Sanchez" : 15,   
#     "Morty Smith" : 12,
#     "Summer Smith" : 10,
#     "Mr. Meeseeks" : 20
# }
# 
# Cree una función llamada precioTotal que calculará el monto total de la compra en función de estos datos. Cuando se llame a la
# función precioTotal(carrito, precios) con los diccionarios proporcionados, se debe obtener el monto total de la compra basado en
# la multiplicación de la cantidad de cada figura por su precio unitario en dólares

def precio_total(carrito, precios):
    lista_carrito = list(carrito.values())
    lista_precios = list(precios.values())
    total = []
    
    for i in range(len(lista_carrito)):
        total_producto = lista_carrito[i] * lista_precios[i]    
        total.append(total_producto)
    suma_total = sum(total)
    
    return(suma_total)

def main():
    carrito = { 
        "Rick Sanchez" : 2, 
        "Morty Smith" : 3, 
        "Summer Smith" : 1,
        "Mr. Meeseeks" : 4
    }
    precios = {
        "Rick Sanchez" : 15,   
        "Morty Smith" : 12,
        "Summer Smith" : 10,
        "Mr. Meeseeks" : 20
    }
    total = precio_total(carrito, precios)
    print(f"El precio total seria: ${total}")
    
main()
# 11. Se tienen dos variables del tipo diccionario, en una de ella se almacena la información de los artículos y la cantidad
# que tiene una persona en un carrito de compras:
# carrito = { 
# "lapiceras" : 12, 
# "borrador" : 1, 
# "carpeta" : 2
# }
# 
# En una segunda variable, se almacenan el stock (cantidad de artículos disponibles) de cada uno de los artículos:
# stock = {
# "lapiceras" : 13, 
# "borrador" : 10, 
# "carpeta" : 3
# }
# 
# Con relación a dicha información, se deberán elaborar las siguientes funciones:  
# • hayStock(articulo, cantidad, stock): Recibe un artículo y verifica si hay stock disponible (retorna True en caso de que
# exista; False en caso contrario). 
# hayStock("borrador", 1, stock) => True
# hayStock("borrador", 13, stock) => False
# 
# • procesarPedido(carrito, stock): Recibe los artículos solicitados en carrito y realiza el descuento de stock
# correspondiente. Debe retornar como resultado el stock actualizado. No afectar la variable recibida como parámetro.
# Utilizando las variables anteriores como ejemplo, debería retornar:
# {'lapiceras': 1, 'borrador': 9, 'carpeta': 1}

def hay_stock(articulo, cantidad, stock):
    
    for arti, cant in stock.items():
        if arti == articulo:
            if cant >= cantidad:
                return True
            else:
                return False
    
def procesar_pedido(carrito, stock):
    nuevo_stock = {}
    aux = []
    i = 0
    
    for cant in carrito.values():
        aux.append(cant)
    for arti, cant in stock.items():
        nuevo_stock[arti] = cant - aux[i]
        i += 1
        
    return nuevo_stock

def main():
    carrito = { 
    "lapiceras" : 12, 
    "borrador" : 1, 
    "carpeta" : 2
    }
    stock = {
    "lapiceras" : 13, 
    "borrador" : 10, 
    "carpeta" : 3
    }
    articulo = input("Ingrese un articulo: ")
    cantidad = int(input("Ingrese la cantidad para verificar si hay stock: "))
    hay_stck = hay_stock(articulo, cantidad, stock)
    print("Hay stock:", hay_stck)
    nuevo_stck = procesar_pedido(carrito, stock)
    print("El nuevo stock es: ", nuevo_stck)
    
main()
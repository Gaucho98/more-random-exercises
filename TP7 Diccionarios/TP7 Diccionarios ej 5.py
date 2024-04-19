# 5. Se debe gestionar los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto,
# precio, cantidad en stock. La tienda dispone de 10 productos distintos. El programa debe ser capaz de:
# . Dar de alta un producto nuevo.
# . Buscar un producto por su nombre.
# . Modificar el stock y precio de un producto dado.

import random

def carga_productos():
    productos = []
    
    for i in range(10):
        producto = {}
        producto["nombre"] = input("Ingrese el nombre del producto: ")
        producto["precio"] = random.randint(3000,4500)
        producto["stock"] = random.randint(0,3000)
        productos.append(producto)
    print("Productos cargados con exito.")
    return productos

def buscar_producto(productos):
    buscados = []
    
    flag = True
    pregunta = input("¿Desea buscar un producto? Y/N: ")
    if pregunta == "y":
        flag = True
    elif pregunta == "n":
        flag = False
    
    while flag == True:
        buscar = input("Ingrese el producto a buscar: ")
        for producto in productos:
            if buscar == producto["nombre"]:
                buscados.append(producto)
        pregunta = input("¿Desea buscar otro producto? Y/N: ")
        if pregunta == "y":
            flag = True
        elif pregunta == "n":
            flag = False
            
    return buscados

def impresion(buscados):
    print("Productos buscados: ")
    for producto in buscados:
        print(f"Producto: {producto['nombre']} - Precio: ${producto['precio']} - Stock: {producto['stock']}")
        
def agregar_productos(productos):
    flag = True
    pregunta = input("¿Desea agregar un producto? Y/N: ")
    if pregunta == "y":
        flag = True
    elif pregunta == "n":
        flag = False
    
    while flag == True:    
        producto = {}
        producto["nombre"] = input("Ingrese el nombre del producto: ")
        producto["precio"] = random.randint(3000,4500)
        producto["stock"] = random.randint(0,3000)
        productos.append(producto)
        pregunta = input("¿Desea agregar otro producto? Y/N: ")
        if pregunta == "y":
            flag = True
        elif pregunta == "n":
            flag = False
    return productos

def impresion2(productos_nuevos):
    print("Lista actualizada con productos nuevos: ")
    for producto in productos_nuevos:
        print(f"Producto: {producto['nombre']} - Precio: ${producto['precio']} - Stock: {producto['stock']}")
        
def modificar_producto(productos_nuevos):
    flag = True
    pregunta = input("¿Desea modificar el stock y precio de un producto? Y/N: ")
    if pregunta == "y":
        flag = True
    elif pregunta == "n":
        flag = False
    while flag == True:    
        prod_modificar = input("¿Que producto desea modificar?")
        for producto in productos_nuevos:
            if producto["nombre"] == prod_modificar:
                producto["precio"] = int(input("Ingrese el nuevo precio: "))
                producto["stock"] = int(input("Ingrese el nuevo stock: "))
        pregunta = input("¿Desea modificar el stock y precio otro producto? Y/N: ")
        if pregunta == "y":
            flag = True
        elif pregunta == "n":
            flag = False
    return productos_nuevos

def impresion3(productos_nuevos):
    print("Lista actualizada de productos modificada: ")
    for producto in productos_nuevos:
        print(f"Producto: {producto['nombre']} - Precio: ${producto['precio']} - Stock: {producto['stock']}")
    
def main():
    productos = carga_productos()
    buscados = buscar_producto(productos)
    impresion(buscados)
    productos_nuevos = agregar_productos(productos)
    impresion2(productos_nuevos)
    productos_modificados = modificar_producto(productos_nuevos)
    impresion3(productos_nuevos)
    
main()
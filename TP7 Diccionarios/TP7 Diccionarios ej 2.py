# 2. Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre, edad, genero, dirección, teléfono),
# los almacene en un diccionario y los muestre. Al realizar dicha muestra, destacar la persona más joven en edad.

def ingreso_datos_personas():
    personas = []
    joven = 200
    
    for i in range(10):
        persona = {}
        persona["Nombre"] = input("Nombre: ")
        persona["Edad"] = int(input("Edad: "))
        persona["Genero"] = input("Genero: ")
        persona["Direccion"] = input("Direccion: ")
        persona["Telefono"] = int(input("Telefono: "))
        personas.append(persona)
        if persona["Edad"] < joven:
            joven = persona["Edad"]
            nom = persona["Nombre"]
            
            
    for persona in personas:
        print(f" Nombre: {persona['Nombre']} - Edad: {persona['Edad']} - Genero: {persona['Genero']} - Direccion: {persona['Direccion']} - Telefono: {persona['Telefono']}")
    print(f"La persona mas joven es {nom}. Edad --> {joven}")
    
def main():
    ingreso_datos_personas()
    
main()

'''
# para probar mas rapido:
import random

def ingreso_datos_personas():
    personas = []
    joven = 200
    
    for i in range(10):
        persona = {}
        persona["Nombre"] = input("Nombre: ")
        persona["Edad"] = random.randint(1,90)
        persona["Genero"] = "m o f"
        persona["Direccion"] = 123
        persona["Telefono"] = 321
        personas.append(persona)
        if persona["Edad"] < joven:
            joven = persona["Edad"]
            nom = persona["Nombre"]
            
            
    for persona in personas:
        print(f" Nombre: {persona['Nombre']} - Edad: {persona['Edad']} - Genero: {persona['Genero']} - Direccion: {persona['Direccion']} - Telefono: {persona['Telefono']}")
    print(f"La persona mas joven es {nom}. Edad --> {joven}")
    
def main():
    ingreso_datos_personas()
    
main()
'''
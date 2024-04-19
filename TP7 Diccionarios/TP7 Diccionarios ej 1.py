# 1. Desarrolle un programa que almacene datos de canciones en formato MP3: Artista, Título, Duración (en segundos), Tamaño del
# fichero (en KB). Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. Debe interrumpirse
# la carga cuando el artista ingresado sea vacío.

def almacenamiento_canciones():
    datos_cancion = []
    
    artista = input("Ingrese el artista: ")
    while artista != "":
        cancion = {}
        cancion["Artista"] = artista
        cancion["Titulo"] = input("Ingrese el titulo: ")
        cancion["Duracion en segundos"] = float(input("Ingrese la duracion en segundos: "))
        cancion["Tamaño en mb"] = int(input("Ingrese el tamaño en mb: "))
        artista = input("Ingrese el artista: ")
        datos_cancion.append(cancion)
    print(datos_cancion)
    
    for cancion in datos_cancion:
        print(f"Artista: {cancion['Artista']} - Titulo: {cancion['Titulo']} - Duracion en segundos: {cancion['Duracion en segundos']} - Tamaño en mb: {cancion['Tamaño en mb']}")
        
def main():
    almacenamiento_canciones()
    
main()
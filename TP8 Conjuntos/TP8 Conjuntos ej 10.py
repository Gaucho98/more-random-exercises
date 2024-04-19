# 10. Eliminar elementos comunes de un diccionario: Crea una función que tome dos diccionarios como argumentos y devuelva
# un nuevo diccionario que contenga solo las claves del primer diccionario que no estén en el segundo diccionario.

def devolver_claves(ciudades1, ciudades2):
    return (ciudades1.keys() - ciudades2.keys())

def main():
    ciudades1 = {
        'Nueva York' : 'Estados Unidos',
        'Madrid' : 'España',
        'Roma' : 'Italia',
        'Vancouver' : 'Canada',
        }
    ciudades2 = {
        'Nueva York' : 'Estados Unidos',
        'Madrid' : 'España',
        'Buenos Aires' : 'Peronland',
        'Tokyo' : 'Japon',
        }
    ciudades_distinas = devolver_claves(ciudades1, ciudades2)
    print(f"Ciudades que estan en el primer diccionario pero no en el segundo: {ciudades_distinas}")

main()
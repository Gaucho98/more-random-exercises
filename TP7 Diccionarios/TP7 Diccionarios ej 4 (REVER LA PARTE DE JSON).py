# 4. Realice un programa que pida datos de personas: nombre, día de nacimiento, mes de nacimiento, y año de nacimiento. Después
# deberá repetir lo siguiente: preguntar un número de mes y mostrar en pantalla los datos de las personas que cumplan los años
# durante ese mes. Terminará de repetirse cuando se teclee vacío en el nombre. Persista y recupere la información en cada ejecución
# en un archivo llamado cumpleaños.json.

def ingreso_datos():
    personas = []
    identificador = 1
    
    nombre = input("Nombre: ")
    while nombre != "":
        persona = {}
        persona["id"] = identificador
        persona["Nombre"] = nombre
        persona["Dia"] = int(input("Dia de nacimiento: "))
        persona["Mes"] = int(input("Mes de nacimiento: "))
        persona["Año"] = int(input("Año de nacimiento: "))
        personas.append(persona)
        mes = int(input("Ingrese un numero de mes: "))
        for i in personas:
            if mes == i["Mes"]:
                print(i)
        identificador += 1
        nombre = input("Nombre: ")
        
def main():
    ingreso_datos()
    
main()
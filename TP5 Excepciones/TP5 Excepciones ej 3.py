# 3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como
# parámetro. Los nombres de los meses deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro de la
# función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a
# través de excepciones.

def deteccion_mes(num):
    i = -1
    tupla_meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    try:
        return tupla_meses[i+num]
    except:
        return ""
    
def main():
    num = int(input("Ingrese un numero de mes: "))
    mes = deteccion_mes(num)
    print(f"El mes ingresado es {mes}.")
    
main()
    
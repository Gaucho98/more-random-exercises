# 8. Sistema de calificaciones: Escribe un programa que permita a los profesores registrar las calificaciones de sus alumnos y
# les permita calcular la nota final. Crea un diccionario para cada alumno, con su legajo como clave y una lista de notas como
# valor. Luego, el programa debe permitir al usuario ingresar las notas para cada alumno y calcular su nota final, basándose
# en un sistema de pesos predeterminado.

def registro_notas():
    alumnos = []
    
    print("Ingrese las notas. Una vez finalizado ingrese como legajo -1.")
    legajo = int(input("Ingrese el legajo del alumno: "))
    while legajo != -1:
        alumno = {}
        alumno['legajo'] = legajo
        notas = []
        i = 0
        for i in range(3):
            i += 1
            nota = int(input(f"Nota {i}: "))
            notas.append(nota)
#         notas_tupla = tuple(notas)
        suma = sum(notas)
        promedio = suma / 3
        alumno['notas'] = promedio
        alumnos.append(alumno)
        legajo = int(input("Ingrese el legajo del alumno: "))
        
    for alumno in alumnos:
        print(f"Alumno {alumno['legajo']} - Nota final: {alumno['notas']}")
    
def main():
    registro_notas()
    
main()
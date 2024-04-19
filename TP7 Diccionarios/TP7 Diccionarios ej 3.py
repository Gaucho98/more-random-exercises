# 3. Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura y 4 notas. Calcular y mostrar el promedio
# de las notas.
import random

def registro_notas():
    alumnos = []
    notas_total = []
    
    for i in range(3):
        alumno = {}
        alumno["Nombre"] = input("Nombre: ")
        alumno["Asignatura"] = input("Asignatura: ")
        notas = []
        for j in range(4):
            nota = random.randint(1,10)
            notas.append(nota)
        tupla_notas = tuple(notas)
        alumno["Notas"] = tupla_notas
        alumnos.append(alumno)
        suma = sum(notas)
        notas_total.append(suma)
        
    for alumno in alumnos:
        print(f"Alumno: {alumno['Nombre']} - Asignatura: {alumno['Asignatura']} - Notas: {alumno['Notas']}")
        
    total = sum(notas_total)
    promedio_notas = total / 4 / len(alumnos)
    print("Promedio de notas: ", promedio_notas)

def main():
    registro_notas()
    
main()
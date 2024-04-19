# 12. En un sistema de control de personal, se tiene dos variables. En una de ellas, se almacena en un conjunto la información
# de los empleados que trabajan en la empresa:
# 
# empleados = { "Oliver", "Gabriela", "Irina"}
# 
# En una segunda variable, se encuentran parametrizadas los días de la semana y quienes asistieron:
# 
# semana = {
#     "lunes" : { "Oliver", "Gabriela", "Irina"},
#     "martes" : { "Oliver", "Irina"},
#     "miércoles" : { "Oliver" }
# }
# 
# Conociendo dicha información, se deberán elaborar las siguientes funciones (que deben incluir dentro de la misma,
# operaciones de conjunto en su resolución): 
#     
# • diasAsistenciaPerfecta(empleados, semana): Que retorne una lista con los días que hubo asistencia perfecta
# (que fueron todos los empleados). Siguiendo el ejemplo, el resultado debería ser:
# ['lunes']
# • diasAusencias(empleados, semana): Debe retornar un diccionario, combinando el día con la lista de quienes faltaron por
# cada día. Siguiendo el ejemplo, el resultado debería ser:
# {'lunes': [], 'martes': ['Gabriela'], 'miércoles': ['Irina', 'Gabriela']}

def dias_asistencia_perfecta(empleados, semana):
    dia_asist_perf = []    
    
    for dia, empleado in semana.items():
        if not empleado ^ empleados:
            dia_asist_perf.append(dia)
    return dia_asist_perf

def diasAusencias(empleados, semana):
    ausencias = {}
    
    for dia, empleado in semana.items():
        ausencias[dia] = list(empleado ^ empleados)        
    return ausencias

def main():
    empleados = {"Oliver", "Gabriela", "Irina"}
    semana = {
        "lunes" : {"Oliver", "Gabriela", "Irina"},
        "martes" : {"Oliver", "Irina"},
        "miércoles" : {"Oliver"}
        }
    dia_asist_perf = dias_asistencia_perfecta(empleados, semana)
    print(dia_asist_perf)
    ausencias = diasAusencias(empleados, semana)
    print(ausencias)
    
main()
# 10.Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción
# indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o
# con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:
# 
# a.Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden
# que llegaron a la clínica.
# b.Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.
# Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

def listado_pacientes():
    lista_paciente = []
    lista_condicion = []
    
    num_afiliado = int(input("Ingrese su numero de afiliado: "))
    while num_afiliado != -1:
        while num_afiliado < 1000 or num_afiliado > 9999:
            num_afiliado = int(input("Error, el numero debe contener 4 digitos. Intente nuevamente: "))
        lista_paciente.append(num_afiliado)
        condicion = int(input("¿Tiene turno? (Ingrese 1) ///¿Viene por una urgencia? (Ingrese 0)"))
        while condicion != 1 and condicion != 0:
            condicion = int(input("Intente nuevamente. ¿Tiene turno? (Ingrese 1) ///¿Viene por una urgencia? (Ingrese 0)"))
        if condicion == 1:
            lista_condicion.append(1)
        elif condicion == 0:
            lista_condicion.append(0)
        num_afiliado = int(input("Ingrese su numero de afiliado: "))
            
    return lista_paciente,lista_condicion

def condicion_pacientes(lp,lc):
    
    for i in range(len(lc)):
        if lc[i] == 0:
            print("Paciente",lp[i],"necesita ser atendido por urgencia")
            
    for j in range(len(lc)):
        if lc[j] == 1:
            print("Paciente",lp[j],"debe ser atendido por turno")
            
def busqueda_afiliado(lp,lc):
    turno = 0
    urgencia = 0

    afiliado = int(input("Ingrese un numero de afiliado: "))
    while afiliado != -1:
        for i in range(len(lp)):
            if afiliado == lp[i] and lc[i] == 1:
                turno += 1
            elif afiliado == lp[i] and lc[i] == 0:
                urgencia += 1
        print("El paciente:",afiliado,"///Fue atendido por turno",turno,"veces. Fue atendido por urgencia",urgencia,"veces.")
        turno = 0
        urgencia = 0
        afiliado = int(input("Ingrese un numero de afiliado: "))
        if afiliado == -1:
            print("Fin del programa.")
        
def main():
    lp,lc = listado_pacientes()
    condicion_pacientes(lp,lc)
    busqueda_afiliado(lp,lc)
    
main()
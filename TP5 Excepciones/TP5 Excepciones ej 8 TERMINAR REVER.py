# 8. Escribe un programa que pida al usuario que ingrese dos números enteros y muestre el resultado de la división del primer
# número por el segundo. Si el segundo número es cero, muestra un mensaje de error y vuelve a solicitar el segundo número
# hasta que sea diferente de cero. Los mismo si el tipo de dato ingresado no es correcto. Con intento de realizar la operación
# se debe mostrar en pantalla la leyenda: «Se ha intentado realizar una división».

def division(n1,n2):
    try:
        res = n1 / n2
        print(f"Resultado: {n1} % {n2} = {res}")
    except ZeroDivisionError:
        n2 = int(input("«Se ha intentado realizar una división» \nIntente nuevamente, ingrese otro numero: "))
        while n2 == 0:
            n2 = int(input("«Se ha intentado realizar una división» \nIntente nuevamente, ingrese otro numero: "))
        res = n1 / n2
        print(f"Resultado: {n1} % {n2} = {res}")
    except:
        n2 = int(input("Dato ingresado incorrecto: "))
        res = n1 / n2
        print(f"Resultado: {n1} % {n2} = {res}")
        
def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    division(num1,num2)
    
main()
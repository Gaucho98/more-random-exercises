def funcion_multiplo3(valor):
    if valor % 3 == 0:
        return valor
    else:
        return "-1"
    
def funcion_cubo(resultado):
    if resultado == "-1":
        return "-1"
    else:
        cubo = resultado ** 3
        return cubo

def main():
    valor = int(input("Ingrese un valor: "))
    resultado = funcion_multiplo3(valor)
    resultado_final = funcion_cubo(resultado)
    print(resultado_final)
    
main()
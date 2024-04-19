# 13. Escriba una función que reciba como parámetro un diccionario en el que se indiquen los tipos de cuenta que tienen los
# distintos clientes de un banco y retorne un diccionario con la cantidad de cuentas abiertas en total:
# 
# Por ejemplo, si se tiene el siguiente diccionario de clientes:
# {
# 'Oliver': {'Caja de ahorro pesos', 'Cuenta corriente pesos'},     
# 'Gabriela': {'Caja de ahorro pesos', 'Caja de ahorro dólares'},     
# 'Irina': {'Caja de ahorro pesos'}
#  }
# 
# Se debería obtener el siguiente resultado:
# {
# 'Caja de ahorro pesos': 3, 
# 'Cuenta corriente pesos': 1, 
# 'Caja de ahorro dólares': 1
# }

def tipo_cuenta(clientes):
    cantidad_cuentas = {}
    
    for cliente, tipo_cuenta in clientes.items():
        for tipo in tipo_cuenta:
            print(tipo)
            if tipo not in cantidad_cuentas:
                cantidad_cuentas[tipo] = 1
            elif tipo in cantidad_cuentas:
                cantidad_cuentas[tipo] += 1
            
    print(cantidad_cuentas)

def main():
    clientes = {
        'Oliver': {'Caja de ahorro pesos', 'Cuenta corriente pesos'},     
        'Gabriela': {'Caja de ahorro pesos', 'Caja de ahorro dólares'},     
        'Irina': {'Caja de ahorro pesos'}
         }
    tipo_cuenta(clientes)
    
main()
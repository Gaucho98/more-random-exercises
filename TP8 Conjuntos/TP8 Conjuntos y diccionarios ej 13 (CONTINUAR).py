def bolas_faltantes(bolas,bolas_buchaca):
    total_bolas = set([])
    
    for numero in bolas.keys():
        total_bolas.add(numero)
        
    return total_bolas ^ bolas_buchaca

def tipos_faltantes(bolas,bolas_buchaca):
    faltantes_tipo = {}
    
    for numero, tipo in bolas.items():
        for ray_lis in tipo.values():
            print(ray_lis)
    
def main():
    bolas_buchaca = {1, 3, 11, 13}
    bolas = {
        1: {"color": "blanco", "tipo": "lisa"},
        2: {"color": "amarillo", "tipo": "lisa"},
        3: {"color": "azul", "tipo": "lisa"},
        4: {"color": "rojo", "tipo": "lisa"},
        5: {"color": "morado", "tipo": "lisa"},
        6: {"color": "naranja", "tipo": "lisa"},
        7: {"color": "verde", "tipo": "lisa"},
        8: {"color": "negro", "tipo": "lisa"},
        9: {"color": "amarillo", "tipo": "rayada"},
        10: {"color": "azul", "tipo": "rayada"},
        11: {"color": "rojo", "tipo": "rayada"},
        12: {"color": "morado", "tipo": "rayada"},
        13: {"color": "naranja", "tipo": "rayada"},
        14: {"color": "verde", "tipo": "rayada"},
        15: {"color": "negro", "tipo": "rayada"}
    }
    faltantes = bolas_faltantes(bolas, bolas_buchaca)
    print(faltantes)
    tipos_faltantes(bolas,bolas_buchaca)
    
main()